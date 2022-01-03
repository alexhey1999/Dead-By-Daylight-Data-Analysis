import cv2
import numpy as np

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