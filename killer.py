import cv2
import numpy as np


def adjustScreenSizeKiller(Screen,bVector):
    widthStartCut = 480
    widthEndCut = 1390
    hightStartCut = 735
    hightEndCut = 275

    upper_white = np.array([256, 256, 256])
    lower_white = np.array([bVector, bVector, bVector])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    WhiteBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    WhiteBackground[:,:,:] = (255,255,255)

    BlackBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    BlackBackground[:,:,:] = (0,0,0)

    result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)

    # result = cv2.blur(result,(3,3))

    
    
    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
    # cv2.imshow("Killer Screen", result)
    return result

def calculateKiller(killerList, location, Screen,show = True):
    mostProbableKiller = None
    mostProbableKillerScore = 0

    # firstrun = False

    for killer in killerList:
        icon = cv2.imread(location+killer)
        icon = cv2.resize(icon, (40, 40),interpolation=cv2.INTER_AREA)

        # if killer == "iconPowers_feralFrenzy.png" and firstrun:
        #     cv2.imshow(killer, icon)
        #     firstrun = False
        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        if maxVal > mostProbableKillerScore:
            mostProbableKillerScore = maxVal
            mostProbableKiller = killer
    if show:
        cv2.imshow("Killer Screen", Screen)

    return mostProbableKiller, mostProbableKillerScore