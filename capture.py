import mss.tools
import mss
import cv2
import numpy as np

regionMonitor1 = {
    "top": 357,
    "left": 656,
    "width": 595,
    "height": 525
}


def captureGame(sct):
    screenshot = sct.grab(regionMonitor1)

    imageColors = cv2.cvtColor(
        np.array(screenshot),
        cv2.COLOR_BGRA2BGR
    )

    return imageColors

def captureGameTest(Screen):
    if Screen == "Mac":
        pass
    else:
        monitor = regionMonitor1

        with mss.mss() as sct:
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
