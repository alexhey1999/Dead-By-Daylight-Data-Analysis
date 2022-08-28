#Handle Imports
import cv2
from os import listdir, rename
import argparse
import pyautogui
import numpy as np
import pytesseract
import PIL.Image as Image
from PIL import ImageGrab
import json
import datetime

path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# path = r'C:\Users\alex.hey\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = path

def imageFix(location):

    imageList = listdir(location)

    for fileName in imageList:

        image = Image.open(location+fileName)
        image = image.convert("RGBA")
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
    parser.add_argument('--brightness', dest='brightness', required=False)
    parser.add_argument('--save', dest='save', required=False)
    parser.add_argument('--constant', dest='constant', required=False)

    # parse args
    args = parser.parse_args()

    if args.imageFix:
        imageFix(args.folder)
        quit()

    if args.brightness:
        bVector = int(calculateBrightnessVector(args.brightness))
    else:
        bVector = int(calculateBrightnessVector(1))
    
    print(bVector)

    # set output file
    killerList = listdir("./Killers/")
    perkList = listdir("./Perks/")
    itemList = listdir("./Items/")
    offeringList = listdir("./Offerings/")
    escapeList = listdir("./Escapes/")

    if args.imgFile:
        imgFile = args.imgFile
        KillerScreen = cv2.imread(imgFile)
        PerkScreen = cv2.imread(imgFile)
        ItemScreen = cv2.imread(imgFile)
        OfferingScreen = cv2.imread(imgFile)
        ScoreScreen = cv2.imread(imgFile)
        EscapeScreen = cv2.imread(imgFile)
        TestingScreen = cv2.imread(imgFile)
    else:
        screenshotName = getImageCapture()

        KillerScreen = cv2.imread('Screenshots/'+screenshotName)
        PerkScreen = cv2.imread('Screenshots/'+screenshotName)
        ItemScreen = cv2.imread('Screenshots/'+screenshotName)
        OfferingScreen = cv2.imread('Screenshots/'+screenshotName)
        ScoreScreen = cv2.imread('Screenshots/'+screenshotName)
        EscapeScreen = cv2.imread('Screenshots/'+screenshotName)
        TestingScreen = cv2.imread('Screenshots/'+screenshotName)

        imgFile = "Screenshots/"+screenshotName

    KillerScreen = adjustScreenSizeKiller(KillerScreen, bVector)
    PerkScreen = adjustScreenSizePerks(PerkScreen, bVector)
    ItemScreen = adjustScreenSizeItems(ItemScreen, bVector)
    OfferingScreen = adjustScreenSizeOfferings(OfferingScreen, bVector)
    ScoreScreen = adjustScreenSizeScores(ScoreScreen, bVector)
    EscapeScreen = adjustScreenSizeEscapes(EscapeScreen, bVector)


    if args.icon:
        icon = args.icon
        testingPerk(icon, "./Perks/", PerkScreen, True)


    if args.testing:
        while True:
            img = ImageGrab.grab(bbox=(70, 100, 350, 170)) #x, y, w, h
            img_np = np.array(img)
            screen = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
            
            cv2.imshow("Testing", screen )
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break

    else:

        killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen)
        perks = calculatePerks(perkList, "./Perks/", PerkScreen)
        items = calculateItems(itemList, "./Items/", ItemScreen)
        offerings = calculateOfferings(offeringList, "./Offerings/", OfferingScreen)
        scores = calculateScores(ScoreScreen)
        escapes = calculateEscapes(escapeList, "./Escapes/", EscapeScreen,bVector)

        print('\n\n\n\n\n\n')
        print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%\n')
        print(f'Perks: {perks}\n')
        print(f'Items: {items}\n')
        print(f'Offerings: {offerings}\n')
        print(f'Scores: {scores}\n')
        print(f'Escapes: {escapes}\n')
        
        if args.save:    
            addDataToStorage(killerPlayed, perks, items, offerings, scores, escapes,"./Outputs/", imgFile)

    if args.forceEnd:
        cv2.destroyAllWindows()
    else:
        while True:
            key = cv2.waitKey(30)
            if key == 27 or key == 0:
                quit()
    
if __name__ == "__main__":
    main()