
import cv2
import numpy as np
import random


def adjustScreenSizeOfferings(Screen,bVector):
    widthStartCut = 415
    widthEndCut = 1450
    hightStartCut = 280
    hightEndCut = 280

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

def calculateOfferings(offeringsList, location, Screen):
    offerings = {}
    size = 50
    cropBorder = 0
    thresholdOriginal = 0.85

    firstrun = True

    underdetectedOfferings = ["iconFavors_bloodyPartyStreamers.png",'iconsFavors_5thAnniversary.png','iconFavors_devoutTanagerWreath.png','iconFavors_strodeRealtyKey.png','iconFavors_fragrantSweetWilliam.png']
    overdetectedOfferings = ["iconFavors_clearReagent.png",'iconFavors_faintReagent.png','iconFavors_hazyReagent.png','iconFavors_murkyReagent.png','iconFavors_vigosShroud.png','iconFavors_shroudOfBinding.png', 'iconFavors_shroudOfSeparation.png','iconFavors_shroudOfUnion.png']
    # overdetectedOfferings = ["iconFavors_bloodyPartyStreamers.png"]

    for item in offeringsList:
        icon = cv2.imread(location+item)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)

        

        if item in overdetectedOfferings:
            threshold = 0.90

        elif item in underdetectedOfferings:
            threshold = 0.70

        elif "mori" in item.lower():
            threshold = 0.85

        else:
            threshold = thresholdOriginal

        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        color = tuple(list(np.random.choice(range(256), size=3)))

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:

            cv2.putText(Screen, item.split("_")[1].split(".")[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(Screen, (x, y), (x + w, y + h), color, 2)

        if len(rectangles) > 0:
            offerings[item.split('_')[1].split('.')[0]] = len(rectangles)

    cv2.imshow("Offerings Screen", Screen)

    return offerings
