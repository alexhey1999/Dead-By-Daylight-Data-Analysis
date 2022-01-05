#Handle Imports
import cv2
from os import listdir
import argparse
import pyautogui
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\alex.hey\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


from killer import *
from items import *
from perks import *
from offerings import *
from scores import *
from testing import *



#Nebula
#dbdicontoolbox://EvaZioNe-Nebula

def getImageCapture():
    count = 0
    with open('Screenshots/previousTests.txt',"r+") as counter:
        count = int(counter.read())
    with open('Screenshots/previousTests.txt',"w") as counter:
        counter.write(str(count+1))


    fileName = f'Test{count}.png'
    print(fileName)
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
    cv2.imwrite('Screenshots/'+fileName, image)
    return fileName
    


def main():
    # create parser
    descStr = "This takes a screenshot of DBD Endgame and then extrapolates perks, offerings, items, scores and ."
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=False)
    parser.add_argument('--icon', dest='icon', required=False)
    parser.add_argument('--forceEnd', dest='forceEnd', required=False)
    parser.add_argument('--testing', dest='testing', required=False)

    # parse args
    args = parser.parse_args()

    # set output file
    killerList = listdir("./Killers/")
    perkList = listdir("./Perks/")
    itemList = listdir("./Items/")
    offeringList = listdir("./Offerings/")

    if args.imgFile:
        imgFile = args.imgFile
        KillerScreen = cv2.imread(imgFile)
        PerkScreen = cv2.imread(imgFile)
        ItemScreen = cv2.imread(imgFile)
        OfferingScreen = cv2.imread(imgFile)
        ScoreScreen = cv2.imread(imgFile)
    else:
        screenshotName = getImageCapture()
        KillerScreen = cv2.imread('Screenshots/'+screenshotName)
        PerkScreen = cv2.imread('Screenshots/'+screenshotName)
        ItemScreen = cv2.imread('Screenshots/'+screenshotName)
        OfferingScreen = cv2.imread('Screenshots/'+screenshotName)
        ScoreScreen = cv2.imread('Screenshots/'+screenshotName)

    KillerScreen = adjustScreenSizeKiller(KillerScreen)
    PerkScreen = adjustScreenSizePerks(PerkScreen)
    ItemScreen = adjustScreenSizeItems(ItemScreen)
    OfferingScreen = adjustScreenSizeOfferings(OfferingScreen)


    if args.icon:
        icon = args.icon
        testingPerk(icon, "./Perks/", PerkScreen, True)


    if args.testing:
        ScoreScreen = adjustScreenSizeScores(ScoreScreen)
        calculateScores(ScoreScreen)
        pass

    else:

        killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen)
        perks = calculatePerks(perkList, "./Perks/", PerkScreen)
        items = calculateItems(itemList, "./Items/", ItemScreen)
        offerings = calculateOfferings(offeringList, "./Offerings/", OfferingScreen)
        print('\n\n\n\n\n\n')
        print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%\n')
        print(f'Perks: {perks}\n')
        print(f'Items: {items}\n')
        print(f'Offerings: {offerings}\n')
    
    if args.forceEnd:
        cv2.destroyAllWindows()
    else:
        while True:
            key = cv2.waitKey(30)
            if key == 27 or key == 0:
                quit()
    
if __name__ == "__main__":
    main()