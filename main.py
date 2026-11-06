import capture
import detection

import time
import mss

with mss.mss() as sct:

    while(True):

        time.sleep(5)

        capture.captureGame("123")

        imageColors = detection.readScreenshot("./screenshots/snake.png")

        colorsArray = detection.colors(imageColors)

        applePosition = detection.colorConditions(200,60,colorsArray,0,1,2)

        appleCenterPosition = (round(applePosition[0].mean()),round(applePosition[1].mean()))


        detection.makeCircle(imageColors, appleCenterPosition, 10)

        colorsArray = detection.colors(imageColors)

        snakePosition = detection.colorConditions(150,20,colorsArray,2,1,0)

        markedSnake = detection.markSnakeBody(snakePosition)

        for i in range(len(markedSnake)):
            detection.makeCircle(imageColors,markedSnake[i],10)

        detection.changeImage("./screenshots/marked_snake.png",imageColors)

    
    


    