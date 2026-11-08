import cv2
import numpy as np

cellsize = 35


def readScreenshot(imagePath):
    imageColors = cv2.imread(f"{imagePath}")
    return imageColors

def colors(imageArray):
    red = imageArray[:, :, 2].astype(int)
    green = imageArray[:, :, 1].astype(int)
    blue = imageArray[:, :, 0].astype(int)

    colorsArray = [red,green,blue]
    return colorsArray
    
def colorConditions(hardColorValue, colorMargin, colorsArray, colorNum1, colorNum2, colorNum3):
    y, x = np.where(
    (colorsArray[colorNum1] > hardColorValue) &
    (colorsArray[colorNum1] > colorsArray[colorNum2] + colorMargin) &
    (colorsArray[colorNum1] > colorsArray[colorNum3] + colorMargin)
    )


    position = [x,y]
    return position
    
def makeCircle(imageColors, positionArray, radius, color):
    cv2.circle(imageColors, positionArray, radius, color, -1)
    return

def markSnakeBody(snakePosition):
    markedSnake = []
    snakeGrid = {}

    for i in range(len(snakePosition[0])):

        cell = (snakePosition[0][i]//cellsize,snakePosition[1][i]//cellsize )

        snakeGrid[cell] = snakeGrid.get(cell,0) + 1

    for cell, count in snakeGrid.items():

        if count < 300:
            continue

        x = cell[0] * cellsize + cellsize//2
        y = cell[1] * cellsize + cellsize//2

        markedSnake.append((x,y))


    return markedSnake

def findSnakeHead(colorsArray):
    eyePositions = {}
    markedEyes = []
    y, x = np.where(
        (colorsArray[0] > 200) &
        (colorsArray[1] > 200) &
        (colorsArray[2] > 200)
    )

    for i in range(len(y)):

        cell = (x[i]//cellsize,y[i]//cellsize)

        eyePositions[cell] = eyePositions.get(cell,0) + 1

    for cell, count in eyePositions.items():

        if count < 100:
            continue
        
        x = cell[0] * cellsize + cellsize//2
        y = cell[1] * cellsize + cellsize//2
    
        markedEyes.append((x,y))
    return markedEyes


def noSnakeHead(prevMarkedHead):
    markedHead = prevMarkedHead
    return markedHead

    



def changeImage(imagePath,imageColors):
    cv2.imwrite(f"{imagePath}", imageColors)


