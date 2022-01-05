import cv2
import numpy as np
import pytesseract

def adjustScreenSizeScores(Screen):
    widthStartCut = 575
    widthEndCut = 1200
    hightStartCut = 310
    hightEndCut = 300

    # print(Screen.shape)
    # hsv = cv2.cvtColor(Screen, cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV", Screen)
    # Threshold of blue in HSV space
    upper_white = np.array([255, 255, 255])
    lower_white = np.array([182, 182, 182])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    result = cv2.bitwise_and(Screen, Screen, mask = mask)


    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
    # cv2.imshow("Screen", result)
    return result

def calculateScores(Screen):
    text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6')
    print(f'Text Extrapolated: {text}')
    firstrun = True
    if firstrun:
        cv2.imshow("Screen", Screen)
        firstrun = False

    return text
