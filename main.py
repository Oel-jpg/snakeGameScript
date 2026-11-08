import capture
import detection
import controls

import time
import mss

move = None
prevMarkedHead = None
board = None

with mss.mss() as sct:


    time.sleep(5)


    while(True):

        # capture.captureGametest("123")

        # imageColors = detection.readScreenshot("./screenshots/snake.png")

        imageColors = capture.captureGame(sct)

        colorsArray = detection.colors(imageColors)

        snakePosition = detection.colorConditions(150,20,colorsArray,2,1,0)

        markedSnake = detection.markSnakeBody(snakePosition)

        for i in range(len(markedSnake)): detection.makeCircle(imageColors,markedSnake[i],10, (255,255,255))

        markedHead = detection.findSnakeHead(colorsArray)

        for i in range(len(markedHead)): detection.makeCircle(imageColors,markedHead[i],5,(0,0,0))

        applePosition = detection.colorConditions(200,60,colorsArray,0,1,2)

        appleCenterPosition = [(round(applePosition[0].mean()),round(applePosition[1].mean()))]

        for i in range(len(appleCenterPosition)): detection.makeCircle(imageColors,appleCenterPosition[i],5,(0,0,0))

        detection.changeImage("./screenshots/marked_snake.png",imageColors)

        if len(markedHead) == 0 and board != None:
            markedHead = detection.noSnakeHead(prevMarkedHead)

        board = controls.BoardGrid(markedSnake,appleCenterPosition,markedHead)

        prevMarkedHead = markedHead

        move = controls.findMove(board, move)

        if move is not None:
            controls.move(move)



        