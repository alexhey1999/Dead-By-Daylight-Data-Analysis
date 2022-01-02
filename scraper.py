#Handle Imports
import cv2
import numpy as np
from os import listdir
import argparse, random

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


def calculateItems(itemList, location, Screen):
    items = {}
    size = 36
    cropBorder = 4
    threshold = 0.85

    # firstrun = True

    for item in itemList:
        icon = cv2.imread(location+item)
        icon = cv2.resize(icon, (size, size),interpolation=cv2.INTER_AREA)
        icon = icon[cropBorder:size-cropBorder , cropBorder:size-cropBorder]

        # if firstrun:
            # cv2.imshow("Screen", Screen)
            # cv2.imshow("Icon", icon)
            # firstrun = False

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
            # cv2.imshow("Item", Screen)
            # print(f'{perk} : {len(rectangles)}')
    # print(perks)
    return items


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

def adjustScreenSizeItems(Screen):
    widthStartCut = 430
    widthEndCut = 1445
    hightStartCut = 310
    hightEndCut = 400

    # print(Screen.shape)
    Screen = Screen[0+hightStartCut:Screen.shape[0]-hightEndCut, 0+widthStartCut:Screen.shape[1]-widthEndCut]
    # cv2.imshow("Screen", Screen)
    return Screen

    
size = 46
threshold = 0.70
cropBorder = 9

def main():
    # create parser
    descStr = "This program converts an image into ASCII art."
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=True)
    parser.add_argument('--icon', dest='icon', required=False)
    parser.add_argument('--forceEnd', dest='forceEnd', required=False)
    parser.add_argument('--testing', dest='testing', required=False)

    # parse args
    args = parser.parse_args()
    imgFile = args.imgFile

    # set output file
    killerList = listdir("./Killers/")
    perkList = listdir("./Perks/")
    itemList = listdir("./Items/")

    KillerScreen = cv2.imread(imgFile)
    PerkScreen = cv2.imread(imgFile)
    ItemScreen = cv2.imread(imgFile)

    KillerScreen = adjustScreenSizeKiller(KillerScreen)
    PerkScreen = adjustScreenSizePerks(PerkScreen)
    ItemScreen = adjustScreenSizeItems(ItemScreen)

    if args.icon:
        icon = args.icon
        testingPerk(icon, "./Perks/", PerkScreen, True)

    if args.testing:
        adjustScreenSizeItems(ItemScreen)
    else:
        killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen)
        perks = calculatePerks(perkList, "./Perks/", PerkScreen)
        items = calculateItems(itemList, "./Items/", ItemScreen)

        print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%')
        print(f'Perks: {perks}')
        print(f'Items: {items}')
    
    if args.forceEnd:
        cv2.destroyAllWindows()
    else:
        while True:
            key = cv2.waitKey(30)
            if key == 27 or key == 0:
                quit()
    
if __name__ == "__main__":
    main()