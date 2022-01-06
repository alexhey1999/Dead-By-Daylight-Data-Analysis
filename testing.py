import cv2
import numpy as np

def testingScreenAdjust(Screen):
    widthStartCut = 160
    widthEndCut = 1550
    hightStartCut = 290
    hightEndCut = 290
    upper_white = np.array([255, 255, 255])
    lower_white = np.array([160, 160, 160])

    mask = cv2.inRange(Screen, lower_white, upper_white)

    result = cv2.bitwise_and(Screen, Screen, mask = mask)
    # print(Screen.shape)

    
    result = result[0+hightStartCut:result.shape[0]-hightEndCut, 0+widthStartCut:result.shape[1]-widthEndCut]
    # cv2.imshow("Screen", result)
    return result



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


def testingBlackAndWhite(perkList,location,Screen):
    perks = {}
    size = 46
    threshold = 0.65
    cropBorder = 0

    firstrun = True

    for perk in perkList:
        icon = cv2.imread(location+perk,cv2.IMREAD_UNCHANGED)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        trans_mask = icon[:,:,3] == 0
        icon[trans_mask] = [0, 0, 0, 0]
        icon = cv2.cvtColor(icon, cv2.COLOR_BGRA2BGR)


        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        if perk == "iconPerks_decisiveStrike.png":
            cv2.imshow("Screen", Screen)
            cv2.imshow("Icon", icon)
            firstrun = False

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