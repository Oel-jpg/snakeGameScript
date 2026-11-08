from detection import cellsize
import pyautogui as pyauto
import time

gridHeight = 15
gridWidth = 17

oppositeDirections = {
    "right" : "left",
    "left" : "right",
    "up" : "down",
    "down": "up"
}

def normalizeToGrid(nums, cellsize):
    r = [(x // cellsize, y// cellsize) for x,y in nums]

    return r

def setBoardPosition(positionList, Board, message):
    for x, y in positionList: Board[y][x] = message
 
def BoardGrid(snakePosition, applePosition, snakeHeadPosition):
    Board = []
    for _ in range(gridHeight):
        Board.append(["None"] * gridWidth)

    snakePosition = normalizeToGrid(snakePosition, cellsize)
    snakeHeadPosition = normalizeToGrid(snakeHeadPosition, cellsize)
    applePosition = normalizeToGrid(applePosition, cellsize)

    setBoardPosition(snakePosition, Board, "Body")
    setBoardPosition(snakeHeadPosition, Board, "Head")
    setBoardPosition(applePosition, Board, "Appl")
        
    return Board        

def findMove(Board, prev):

    if prev == None:
        move = "right"

    for y, row in enumerate(Board):
        if "Head" in row:
            head = (row.index("Head"), y)

        if "Appl" in row:
            apple = (row.index("Appl"), y)

    xdelta = head[0] - apple[0]
    ydelta = head[1] - apple[1]


    if xdelta > 0:
        move = "left"
    elif xdelta < 0:
        move = "right"

    if xdelta == 0:
        if ydelta > 0:
            move = "up"
        if ydelta < 0:
            move = "down"

    if oppositeDirections[move] == prev:
        move = "up"

    if prev != move:
        return move

    return 

def move(move):
    pyauto.press(move)
    return
    



    
