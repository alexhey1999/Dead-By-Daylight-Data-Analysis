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
    lower_white = np.array([155, 155, 155])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    result = cv2.bitwise_and(Screen, Screen, mask = mask)

    result = cv2.bitwise_not(result)
 
    # result = cv2.GaussianBlur(result,(3,3),cv2.BORDER_DEFAULT)

    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
 
    
 
    # cv2.imshow("Screen", result)
    return result

def calculateScores(Screen):
    # text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
    text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6')
    # print(f'Text Extrapolated: \n{text}')
    text = text.replace('.','').replace(' ','').split('\n')
    text = [i for i in text if i]
    print(f'Text Extrapolated: \n{text}')

    scores = {}

    for i,score in enumerate(text):
        if i == 4:
            try:
                int(score)
                scores['Killer'] = int(score)
            except:
                scores['Killer'] = "NaN"

        else:
            try:
                int(score)
                scores[f'Player {i+1}'] = int(score)
            except:
                scores[f'Player {i+1}'] = "NaN"

    firstrun = True
    if firstrun:
        cv2.imshow("Screen", Screen)
        firstrun = False

    print(scores)


    return text
