from detection import cellsize
import pyautogui as pyauto
import time

gridHeight = 15
gridWidth = 17

def findmove(snakehead, path):
    if not path:
        return None

    headX, headY = snakehead
    nextX, nextY = path[0]

    directions = {
        (1, 0): "right",
        (-1, 0): "left",
        (0, 1): "down",
        (0, -1): "up",
    }

    return directions.get((nextX - headX, nextY - headY))
    
def move(move):
    pyauto.press(move)




       

    



    
