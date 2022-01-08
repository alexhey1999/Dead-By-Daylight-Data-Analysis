#Handle Imports
import cv2
from os import listdir
import argparse
import pyautogui
import numpy as np
import pytesseract
import PIL.Image as Image

path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# path = r'C:\Users\alex.hey\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = path

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

def imageFix(location):
    imageList = listdir(location)
    for fileName in imageList:
        image = Image.open(location+fileName)
        image.convert("RGBA")
        canvas = Image.new('RGBA', image.size, (0,0,0,255)) # Empty canvas colour (r,g,b,a)
        canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
        canvas.save(str(location+fileName), format="PNG")


def main():
    # create parser
    descStr = "This takes a screenshot of DBD Endgame and then extrapolates perks, offerings, items, scores and ."
    parser = argparse.ArgumentParser(description=descStr)

    # add expected arguments
    parser.add_argument('--file', dest='imgFile', required=False)
    parser.add_argument('--icon', dest='icon', required=False)
    parser.add_argument('--forceEnd', dest='forceEnd', required=False)
    parser.add_argument('--testing', dest='testing', required=False)
    parser.add_argument('--imageFix', dest='imageFix', required=False)
    parser.add_argument('--folder', dest='folder', required=False)

    # parse args
    args = parser.parse_args()

    if args.imageFix:
        imageFix(args.folder)
        quit()
    

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
        # OfferingScreen = cv2.imread(imgFile)
        ScoreScreen = cv2.imread(imgFile)
        TestingScreen = cv2.imread(imgFile)
    else:
        screenshotName = getImageCapture()

        KillerScreen = cv2.imread('Screenshots/'+screenshotName)
        PerkScreen = cv2.imread('Screenshots/'+screenshotName)
        ItemScreen = cv2.imread('Screenshots/'+screenshotName)
        # OfferingScreen = cv2.imread('Screenshots/'+screenshotName)
        ScoreScreen = cv2.imread('Screenshots/'+screenshotName)
        TestingScreen = cv2.imread('Screenshots/'+screenshotName)

    KillerScreen = adjustScreenSizeKiller(KillerScreen)
    PerkScreen = adjustScreenSizePerks(PerkScreen)
    ItemScreen = adjustScreenSizeItems(ItemScreen)
    # OfferingScreen = adjustScreenSizeOfferings(OfferingScreen)
    ScoreScreen = adjustScreenSizeScores(ScoreScreen)

    if args.icon:
        icon = args.icon
        testingPerk(icon, "./Perks/", PerkScreen, True)


    if args.testing:
        screen = testingScreenAdjust(TestingScreen)
        perks = testingBlackAndWhite(perkList,"./Perks/",screen)
        print(perks)
        pass

    else:

        killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen)
        perks = calculatePerks(perkList, "./Perks/", PerkScreen)
        items = calculateItems(itemList, "./Items/", ItemScreen)
        # offerings = calculateOfferings(offeringList, "./Offerings/", OfferingScreen)
        scores = calculateScores(ScoreScreen)

        print('\n\n\n\n\n\n')
        print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%\n')
        print(f'Perks: {perks}\n')
        print(f'Items: {items}\n')
        # print(f'Offerings: {offerings}\n')
        print(f'Scores: {scores}\n')


    if args.forceEnd:
        cv2.destroyAllWindows()
    else:
        while True:
            key = cv2.waitKey(30)
            if key == 27 or key == 0:
                quit()
    
if __name__ == "__main__":
    main()