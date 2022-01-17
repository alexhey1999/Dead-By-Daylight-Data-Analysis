import cv2
import numpy as np
import random

def adjustScreenSizePerks(Screen,bVector):
    widthStartCut = 170
    widthEndCut = 1500
    hightStartCut = 280
    hightEndCut = 270

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
    # cv2.imshow("Perk Screen", result)
    return result

def calculatePerks(perkList,location,Screen):
    perks = {}
    size = 50
    thresholdOriginal = 0.65
    cropBorder = 0

    firstrun = True

    entropyList = []

    for perk in perkList:
        icon = cv2.imread(location+perk)
        
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA )

        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]


        underdetectedPerks = ["iconPerks_BoonExponential.png","iconPerks_trailOfTorment.png","iconPerks_dragonsGrip.png","iconPerks_Deadlock.png",'iconPerks_discordance.png','iconPerks_hexRetribution.png','iconPerks_camaraderie.png','iconPerks_bloodWarden.png','iconPerks_surveillance.png','iconPerks_FastTrack.png']

        vUnderdetectedPerks = ['iconPerks_NoWayOut.png',"iconPerks_BoonCircleOfHealing.png",'iconPerks_corruptIntervention.png','iconPerks_BoonShadowStep.png']

        noDetection = ['iconPerks_rememberMe.png']

        overdetectedPerks = ["iconPerks_calmSpirit.png",'iconPerks_flipFlop.png','iconPerks_mettleOfMan.png','iconPerks_popGoesTheWeasel.png','iconPerks_deception.png','iconPerks_premonition.png','iconPerks_alert.png','iconPerks_corruptIntervention.png']

        if perk in vUnderdetectedPerks:
            threshold = 0.53
        elif perk in underdetectedPerks:
            threshold = 0.63
        elif perk in noDetection:
            threshold = 0.5
        elif perk in overdetectedPerks:
            threshold = 0.70
        else:
            threshold = thresholdOriginal

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)


        rectangles = []

        # testingPerkList = ["iconPerks_DeadHard.png","iconPerks_BoonCircleOfHealing.png","iconPerks_bond.png"]

        # if perk in testingPerkList:
            # cv2.imshow("Perk", icon)

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), size-cropBorder,size-cropBorder])
            rectangles.append([int(x), int(y), size-cropBorder,size-cropBorder])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        color = tuple(list(np.random.choice(range(256), size=3)))

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:

            cv2.putText(Screen, perk.split("_")[1].split(".")[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(Screen, (x, y), (x + w, y + h), color, 2)

        if len(rectangles) > 0:
            perks[perk.split('_')[1].split('.')[0]] = len(rectangles)


    cv2.imshow("Perk Screen ", Screen)

    return perks
