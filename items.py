import cv2
import numpy as np


def adjustScreenSizeItems(Screen,bVector):
    widthStartCut = 480
    widthEndCut = 1390
    hightStartCut = 300
    hightEndCut = 400

    upper_white = np.array([256, 256, 256])
    lower_white = np.array([bVector, bVector, bVector])


    mask = cv2.inRange(Screen, lower_white, upper_white)

    WhiteBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    WhiteBackground[:,:,:] = (255,255,255)

    BlackBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    BlackBackground[:,:,:] = (0,0,0)

    result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)

    Screen = result
    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

def calculateItems(itemList, location, Screen):
    items = {}
    size = 40
    cropBorder = 2
    threshold = 0.85

    for item in itemList:
        icon = cv2.imread(location+item)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        #Perk Count
        if len(rectangles) > 0:
            items[item] = len(rectangles)
           
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)

    cv2.imshow("Item Screen", Screen)

    return items
