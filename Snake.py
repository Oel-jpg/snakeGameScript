import mss
import mss.tools 
import time 
import cv2
import numpy as np
import pyautogui as pyauto

regionMonitor1 = {"top": 332, "left": 656, "width": 595, "height": 525 }
cellsize = 35

def captureGame(Screen):
    if Screen == "Mac":
        pass
    else:
        monitor = regionMonitor1
    
        img = sct.grab(monitor)

        mss.tools.to_png(
            img.rgb,
            img.size,
            output="./screenshots/snake.png"
        )

    return 

# def testGrid(pixels):
#     with mss.mss() as sct:    
#         for x in range(0, imageColors.shape[1], pixels):
#         cv2.line(
#             imageColors,
#             (x, 0),
#             (x, imageColors.shape[0]),
#             (0, 0, 255),
#             1
#         )
#     return


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
    
def makeCircle(imageColors, positionArray, radius):
    cv2.circle(imageColors, positionArray, radius, (255,255,255), -1)
    return

def markSnakeBody(snakePosition):
    markedSnake = []
    snakeGrid = {}

    for i in range(len(snakePosition[0])):
        snakePosition[0][i] = snakePosition[0][i]//cellsize
        snakePosition[1][i] = snakePosition[1][i]//cellsize

        cell = (snakePosition[0][i],snakePosition[1][i] )

        snakeGrid[cell] = snakeGrid.get(cell,0) + 1

    for cell, count in snakeGrid.items():

        if count < 100:
            continue

        x = cell[0] * cellsize + cellsize//2
        y = cell[1] * cellsize + cellsize//2

        markedSnake.append((x,y))

    return markedSnake






with mss.mss() as sct:

    while(True):

        time.sleep(5)

        captureGame("123")

        imageColors = readScreenshot("./screenshots/snake.png")

        colorsArray = colors(imageColors)

        applePosition = colorConditions(200,60,colorsArray,0,1,2)

        appleCenterPosition = (round(applePosition[0].mean()),round(applePosition[1].mean()))


        makeCircle(imageColors, appleCenterPosition, 10)

        colorsArray = colors(imageColors)

        snakePosition = colorConditions(150,20,colorsArray,2,1,0)

        markedSnake = markSnakeBody(snakePosition)

        for i in range(len(markedSnake)):
            makeCircle(imageColors,markedSnake[i],10)

        cv2.imwrite("./screenshots/marked_snake.png", imageColors)

    
    


    