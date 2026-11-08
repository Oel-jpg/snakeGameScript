class Node:
    def __init__(self, data):
        self.data = data
        self.updateNodeCost(float("inf"), 0)

    def updateNodeCost(self, gCost, hCost):
        self.gCost = gCost
        self.hCost = hCost
        self.setFCost()

    def setFCost(self):
        self.fCost = self.gCost + self.hCost


class Grid:
    def __init__(self, height, width, cellsize):
        self.width = width
        self.height = height
        self.cellsize = cellsize
        self.board = self.makeGrid()
        self.apple = None
        self.head = None


    
    
    @staticmethod
    def normalizeToGrid(nums, cellsize):
        r = [(x // cellsize, y// cellsize) for x,y in nums]
        return r

    def setBoardPosition(self, positionList, message):
        for x, y in positionList: self.board[y][x].data = message

    def makeGrid(self):
        board = []
        for _ in range(self.height):
            row = [Node(None) for _ in range(self.width)]
            board.append(row)
        return board

    def setGrid(self, snakePosition, applePosition, snakeHeadPosition):
        snakePosition = self.normalizeToGrid(snakePosition, self.cellsize)
        applePosition = self.normalizeToGrid(applePosition, self.cellsize)
        snakeHeadPosition = self.normalizeToGrid(snakeHeadPosition, self.cellsize)

        self.setBoardPosition(snakePosition, "Body")
        self.setBoardPosition(applePosition, "Appl")
        self.setBoardPosition(snakeHeadPosition, "Head")

        self.setAppleHead()


    def getAppleHead(self):
        for y, row in enumerate(self.board):
            for x, node in enumerate(row):
                if node.data == "Head":
                    head = (x,y)
                elif node.data == "Appl":
                    apple = (x,y)
        return (apple, head)

    def setAppleHead(self):
        self.apple = self.getAppleHead()[0]
        self.head = self.getAppleHead()[1]

    def findNextNode(self, current, openCells, cameFrom):
        x,y = current
        toSearch = []
        
        for nx, ny in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if not (0 <= nx < self.width and 0 <= ny < self.height):
                continue

            node = self.board[ny][nx]

            if node.data == "Body":
                continue

            toSearch.append((nx,ny))

        newGCost = self.board[y][x].gCost + 1

        for nx,ny in toSearch:
            neighbor = self.board[ny][nx]

            if newGCost < neighbor.gCost:
                hCost = abs(self.apple[0] - nx) + abs(self.apple[1] - ny)
                neighbor.updateNodeCost(newGCost, hCost)
                cameFrom[(nx,ny)] = current
                openCells.add((nx,ny))

        return

    def findPath(self):
        for row in self.board:
            for node in row:
                node.updateNodeCost(float("inf"), 0)

        headX, headY = self.head
        appleX, appleY = self.apple
        headH = abs(appleX - headX) + abs(appleY - headY)
        self.board[headY][headX].updateNodeCost(0, headH)

        openCells = {self.head}
        cameFrom = {}

        def getFCost(position):
            x, y = position
            return self.board[y][x].fCost

        while openCells:
            current = min(openCells, key=getFCost)
            openCells.remove(current)

            if current == self.apple:
                path = []
                while current != self.head:
                    path.append(current)
                    current = cameFrom[current]
                return path[::-1]

            self.findNextNode(current, openCells, cameFrom)

        return []


        









    





    def displayGrid(self):
        for row in self.board:
            cells = [node.data if node.data is not None else "." for node in row]
            print(" ".join(f"{cell:>4}" for cell in cells))
            
