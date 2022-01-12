import cv2
import numpy as np
import random


def adjustScreenSizeItems(Screen,bVector):
    widthStartCut = 480
    widthEndCut = 1390
    hightStartCut = 280
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
    size = 42
    cropBorder = 2
    thresholdOriginal = 0.80

    issueItems = ['iconItems_partyPopper.png','iconItems_chineseFirecracker.png','iconItems_winterEventFirecracker.png']

    for item in itemList:
        icon = cv2.imread(location+item)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        if "key" in item.lower():
            threshold = 0.90
        elif "flashlight" in item.lower():
            threshold = 0.75
        elif "map" in item.lower():
            threshold = 0.85
        elif "toolbox" in item.lower():
            threshold = 0.88
        elif "aid" in item.lower() or "medkit" in item.lower():
            # print("aid")
            threshold = 0.85
        elif item in issueItems:
            threshold = 0.70
        else:
            threshold = thresholdOriginal

        # threshold = thresholdOriginal

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.3)

        color = tuple(list(np.random.choice(range(256), size=3)))

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:

            cv2.putText(Screen, item.split("_")[1].split(".")[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(Screen, (x, y), (x + w, y + h), color, 2)

        if len(rectangles) > 0:
            items[item.split('_')[1].split('.')[0]] = len(rectangles)
            # cv2.imshow(item, icon)
        
           
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)

    cv2.imshow("Item Screen", Screen)

    return items
