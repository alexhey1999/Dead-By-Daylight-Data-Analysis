import cv2

def adjustScreenSizeKiller(Screen):
    widthStartCut = 435
    widthEndCut = 1445
    hightStartCut = 720
    hightEndCut = 310

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

def calculateKiller(killerList, location, Screen):
    mostProbableKiller = None
    mostProbableKillerScore = 0

    for killer in killerList:
        icon = cv2.imread(location+killer)
        icon = cv2.resize(icon, (37, 37),interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        if maxVal > mostProbableKillerScore:
            mostProbableKillerScore = maxVal
            mostProbableKiller = killer

    return mostProbableKiller, mostProbableKillerScore