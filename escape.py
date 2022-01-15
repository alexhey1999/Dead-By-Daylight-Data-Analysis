import cv2
import numpy as np
import random

def adjustScreenSizeEscapes(Screen,bVector):
    bVector = int(bVector*0.9)
    widthStartCut = 800
    widthEndCut = 1050
    hightStartCut = 280
    hightEndCut = 380

    upper_white = np.array([255, 255, 255])
    lower_white = np.array([bVector, bVector, bVector])


    mask = cv2.inRange(Screen, lower_white, upper_white)

    result = cv2.bitwise_and(Screen, Screen, mask = mask)

    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
 
    # cv2.imshow("Scores", result)
    return result

def calculateEscapes(escapeList,location,Screen,bVector):
    offerings = {}

    thresholdOriginal = 0.80

    firstrun = True

    for item in escapeList:
        icon = cv2.imread(location+item)
        # print(icon.shape)

        if item == "alive.png":
            height = 48
            width = 40
            threshold = thresholdOriginal

            
        elif item == "death.png":
            height = 45
            width = 38
            threshold = 0.75
            
        elif item == "disconnected.png":
            height = 35
            width = 52
            threshold = 0.75

        elif item == "escape.png":
            height = 40
            width = 35
            threshold = 0.75

        elif item == "sacrificed.png":
            height = 57
            width = 40
            threshold = 0.75

        else:
            height = 58
            width = 40
            threshold = 0.75
            print(f'Unknown Image {item}')

        
        upper_white = np.array([255, 255, 255])
        lower_white = np.array([bVector, bVector, bVector])


        mask = cv2.inRange(icon, lower_white, upper_white)

        icon = cv2.bitwise_and(icon, icon, mask = mask)

        icon = cv2.resize(icon, (width,height),interpolation=cv2.INTER_AREA)
        
        # icon = icon[]

        # cv2.imshow(item, icon)

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), width,height])
            rectangles.append([int(x), int(y), width,height])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        color = tuple(list(np.random.choice(range(256), size=3)))

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:

            cv2.putText(Screen, item, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(Screen, (x, y), (x + w, y + h), color, 2)

        if len(rectangles) > 0:
            offerings[item.split('.')[0]] = len(rectangles)

    cv2.imshow("Escape Screen", Screen)

    return offerings
