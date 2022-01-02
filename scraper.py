#Handle Imports
import cv2
import numpy as np
from os import listdir
import warnings

#Nebula
#dbdicontoolbox://EvaZioNe-Nebula

#dbdicontoolbox://EvaZioNe-Nebula-(Colored)


#Requires dbdicontoolbox://EvaZioNe-Simple-Border-Pack
#Pack Name : EvaZioNe-Simple-Border-Pack

#Required dbdicontoolbox://Shirbler-Toon-Pack
#Pack Name : Shirbler-Toon-Pack

#required dbdicontoolbox://RealSlowLoris-Shattered-(Reimagined)


#Potential Pack List
#EvaZioNe-Simple-Border-Pack
#Shirbler-Toon-Pack
#Pixel Icons
#dbdicontoolbox://Toon-Windows-Emoji-UI
#dbdicontoolbox://Sno7h-+-EvaZionE-Nostalgia-Colored-Pack
#dbdicontoolbox://Kodiak__Killer-Split-Personality

def calculateKiller(killerList, Location, Screen):
    mostProbableKiller = None
    mostProbableKillerScore = 0

    for killer in killerList:
        icon = cv2.imread("./Killers/"+killer)
        icon = cv2.resize(icon, (37, 37),interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(Screen, icon, cv2.TM_CCOEFF_NORMED)
        minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
        if maxVal > mostProbableKillerScore:
            mostProbableKillerScore = maxVal
            mostProbableKiller = killer

        # cv2.imshow(killer, result)
        # cv2.imshow("Icon", icon)
        # cv2.waitKey(30)        
    
    

    # print("Killer Played: " + mostProbableKiller)
    # print("Confirmation: " + str(round(mostProbableKillerScore * 100,2)) + "%")

    return mostProbableKiller, mostProbableKillerScore


def calculatePerks(perkList,location, Screen):
    global size, threshold, cropBorder
    perks = {}
    for perk in perkList:
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
        if len(rectangles) > 0:
            perks[perk] = len(rectangles)
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)
    return perks




def testingPerk(perk,location,Screen,force=False):
    global size, threshold, cropBorder

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


def adjustScreenSizePerks(Screen):
    widthStartCut = 160
    widthEndCut = 1550
    hightStartCut = 290
    hightEndCut = 290

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

def adjustScreenSizeKiller(Screen):
    widthStartCut = 435
    widthEndCut = 1445
    hightStartCut = 720
    hightEndCut = 310

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen
    
size = 46
threshold = 0.7
cropBorder = 9

def main():

    killerList = listdir("./Killers/")
    perkList = listdir("./Perks/")
    KillerScreen = cv2.imread('test1.jpg')
    PerkScreen = cv2.imread('test1.jpg')

    KillerScreen = adjustScreenSizeKiller(KillerScreen)

    PerkScreen = adjustScreenSizePerks(PerkScreen)

    killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen)
    perks = calculatePerks(perkList, "./Perks/", PerkScreen)

    print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%')
    print(f'Perks: {perks}')
    
    # testPerk = "iconPerks_BoonCircleOfHealing.png"
    #testPerk = "iconPerks_botanyKnowledge.png"
    #testPerk = "iconPerks_dejaVu.png"
    #testPerk = "iconPerks_ironGrasp.png"
    #testPerk = "iconPerks_leftBehind.png"
    #testPerk = "iconPerks_painResonance.png"
    #testPerk = "iconPerks_theThirdSeal.png"
    #testPerk = "iconPerks_TerritorialImperative.png"
    #testPerk = "iconPerks_objectOfObsession.png"
    #testPerk = "iconPerks_corruptIntervention.png"
    # testPerk = "iconPerks_gearHead.png"
    # testPerk = "iconPerks_enduring.png"
    
    # testingPerk(testPerk, "./Perks/", Screen, True)
    
    while True:
        key = cv2.waitKey(30)
        if key == 27 or key == 0:
            quit()
    
if __name__ == "__main__":
    main()