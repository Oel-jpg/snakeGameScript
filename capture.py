import mss.tools
import mss
regionMonitor1 = {"top": 332, "left": 656, "width": 595, "height": 525 }



def captureGame(Screen):
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
