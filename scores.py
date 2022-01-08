import cv2
import numpy as np
import pytesseract

def adjustScreenSizeScores(Screen):
    widthStartCut = 650
    widthEndCut = 1120
    hightStartCut = 260
    hightEndCut = 260

    # print(Screen.shape)
    # hsv = cv2.cvtColor(Screen, cv2.COLOR_BGR2HSV)
    # cv2.imshow("HSV", Screen)
    # Threshold of blue in HSV space
    upper_white = np.array([255, 255, 255])
    lower_white = np.array([115, 115, 115])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    result = cv2.bitwise_and(Screen, Screen, mask = mask)

    result = cv2.bitwise_not(result)
 
    # result = cv2.GaussianBlur(result,(3,3),cv2.BORDER_DEFAULT)

    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
 
    cv2.imshow("Scores", result)
    return result

def checkPlayerScore(scores,playerScore,player):
    try:
        scores[player] = int(playerScore)
    except:
        scores[player] = "NaN"

def calculateScores(Screen):
    # text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6')
    # print(f'Text Extrapolated: \n{text}')
    text = text.replace('.','').replace(' ','').split('\n')
    text = [i for i in text if i]
    print(f'Text Extrapolated: \n{text}')

    scores = {}

    try:
        checkPlayerScore(scores,text[0],"Player1")
        checkPlayerScore(scores,text[1],"Player2")
        checkPlayerScore(scores,text[2],"Player3")
        checkPlayerScore(scores,text[4],"Player4")
        checkPlayerScore(scores,text[5],"Killer")
    except:
        print("Error")

    firstrun = False
    if firstrun:
        cv2.imshow("Screen", Screen)
        firstrun = False


    return scores
