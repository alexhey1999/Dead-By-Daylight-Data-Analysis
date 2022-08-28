from math import nan
import cv2
import numpy as np
import PIL.Image as Image
import random
from numpy.core.numeric import NaN
from scipy.stats import entropy

def testingScreenAdjust(Screen):
    print(Screen.shape)
    widthStartCut = 170
    widthEndCut = 1500
    hightStartCut = 280
    hightEndCut = 270

    upper_white = np.array([256, 256, 256])
    lower_white = np.array([105, 105, 105])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    WhiteBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    WhiteBackground[:,:,:] = (255,255,255)

    BlackBackground = np.zeros((Screen.shape[0], Screen.shape[1], 3), dtype=np.uint8)
    BlackBackground[:,:,:] = (0,0,0)

    result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)

    # result = cv2.blur(result,(3,3))
    
    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
    cv2.imshow("Screen", result)
    return result





def testingBlackAndWhite(perkList,location,Screen):
    perks = {}
    size = 50
    thresholdOriginal = 0.65
    cropBorder = 0

    firstrun = True
    #convert screen to black and white
    entropyList = []

    for perk in perkList:
        icon = cv2.imread(location+perk)
        
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA )


        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        # cv2.imshow(perk, icon)

        # ent = entropy(icon)

        # f = []
        # for i in ent:
        #     if not(np.isnan(i[0])):
        #         f.append(i) 
        # entropyList.append(np.average(f))

        issuePerks = ["iconPerks_BoonCircleOfHealing.png","iconPerks_BoonExponential","iconPerks_trailOfTorment.png","iconPerks_dragonsGrip.png"]

        if perk in issuePerks:
            threshold = 0.49
        else:
            threshold = thresholdOriginal

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)


        rectangles = []

        testingPerkList = ["iconPerks_DeadHard.png","iconPerks_BoonCircleOfHealing.png","iconPerks_bond.png"]

        if perk in testingPerkList:
            # cv2.imshow("Screen", Screen)
            # print(icon)

            #Double Size of Icon
            # icon = cv2.resize(icon, (size*2, size*2),interpolation=cv2.INTER_AREA )
            cv2.imshow("Icon", icon)

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), size-cropBorder,size-cropBorder])
            rectangles.append([int(x), int(y), size-cropBorder,size-cropBorder])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)
        
        color = tuple(list(np.random.choice(range(256), size=3)))

        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:
            # cv2.putText()

            cv2.putText(Screen, perk.split("_")[1].split(".")[0], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(Screen, (x, y), (x + w, y + h), color, 2)



        if len(rectangles) > 0:
            perks[perk] = len(rectangles)

    #double screen size to make it easier to see
    # Screen = cv2.resize(Screen, (Screen.shape[1]*2, Screen.shape[0]*2),interpolation=cv2.INTER_AREA)

    cv2.imshow("Screen", Screen)


    # mymin = np.min(entropyList)
    # min_positions = [i for i, x in enumerate(entropyList) if x == mymin]

    # mymax = np.max(entropyList)
    # max_positions = [i for i, x in enumerate(entropyList) if x == mymax]

    return perks


#Issue Perks

# testPerk = "iconPerks_BoonCircleOfHealing.png"
# testPerk = "iconPerks_botanyKnowledge.png"
# testPerk = "iconPerks_dejaVu.png"
# testPerk = "iconPerks_ironGrasp.png"
# testPerk = "iconPerks_leftBehind.png"
# testPerk = "iconPerks_painResonance.png"
# testPerk = "iconPerks_theThirdSeal.png"
# testPerk = "iconPerks_TerritorialImperative.png"
# testPerk = "iconPerks_objectOfObsession.png"
# testPerk = "iconPerks_corruptIntervention.png"
# testPerk = "iconPerks_gearHead.png"
# testPerk = "iconPerks_enduring.png"






































def testingPerk(perk,location,Screen,size,threshold,cropBorder,force=False):
    

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
    # print(f'{perk} : {len(rectangles)}')

    for (x, y, w, h) in rectangles:
        cv2.rectangle(Screen, (x, y), (x + w, y + h), (0, 255, 0), 2)

    if len(rectangles) > 0 or force:
        cv2.imshow("Perk", Screen)
        cv2.imshow("Icon", icon)