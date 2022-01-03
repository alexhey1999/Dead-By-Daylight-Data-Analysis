import cv2
import numpy as np

def adjustScreenSizePerks(Screen):
    widthStartCut = 160
    widthEndCut = 1550
    hightStartCut = 290
    hightEndCut = 290

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

def calculatePerks(perkList,location,Screen):
    perks = {}
    size = 46
    threshold = 0.67
    cropBorder = 8

    for perk in perkList:
        icon = cv2.imread(location+perk)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]
        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

        #Perk Count
        if len(rectangles) > 0:
            perks[perk] = len(rectangles)
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)
    return perks