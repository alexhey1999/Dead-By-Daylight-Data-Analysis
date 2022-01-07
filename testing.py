import cv2
import numpy as np
import PIL.Image as Image

def testingScreenAdjust(Screen):
    print(Screen.shape)
    widthStartCut = 160
    widthEndCut = 1550
    hightStartCut = 290
    hightEndCut = 300

    upper_white = np.array([256, 256, 256])
    lower_white = np.array([145, 145, 145])

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
    size = 47
    threshold = 0.60
    cropBorder = 4

    firstrun = True
    #convert screen to black and white

    for perk in perkList:
        icon = cv2.imread(location+perk)
        
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA )



        # upper_white = np.array([255, 255, 255])
        # lower_white = np.array([90, 90, 90])

        # mask = cv2.inRange(icon, lower_white, upper_white)

        # WhiteBackground = np.zeros((icon.shape[0], icon.shape[1], 3), dtype=np.uint8)
        # WhiteBackground[:,:,:] = (255,255,255)

        # BlackBackground = np.zeros((icon.shape[0], icon.shape[1], 3), dtype=np.uint8)
        # BlackBackground[:,:,:] = (0,0,0)



        # result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)

        # icon = cv2.blur(icon,(3,3))

        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        # cv2.imshow(perk, icon)

        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        yloc, xloc = np.where(result >= threshold)
        rectangles = []

        if perk == "iconPerks_quickAndQuiet.png":
            cv2.imshow("Screen", Screen)
            cv2.imshow("Icon", icon)
            firstrun = False

        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])
            rectangles.append([int(x-cropBorder), int(y-cropBorder), size,size])

        rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

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