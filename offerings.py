import cv2
import numpy as np


def adjustScreenSizeOfferings(Screen):
    widthStartCut = 370
    widthEndCut = 1495
    hightStartCut = 310
    hightEndCut = 300

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

def calculateOfferings(offeringsList, location, Screen):
    offerings = {}
    size = 45
    cropBorder = 7
    threshold = 0.90

    firstrun = False

    for item in offeringsList:
        icon = cv2.imread(location+item)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]
        if firstrun:
                cv2.imshow("Screen", Screen)
                cv2.imshow("Icon", icon)
                firstrun = False
        

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        #Perk Count
        if len(rectangles) > 0:
            offerings[item] = len(rectangles)
            
            # cv2.imshow("Item", Screen)
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)
    return offerings
