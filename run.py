#Handle Imports
import cv2
from os import kill, listdir
import argparse
import pyautogui
import numpy as np
import pytesseract
import PIL.Image as Image
import json
import datetime

# path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
path = r'C:\Users\alex.hey\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

pytesseract.pytesseract.tesseract_cmd = path

from killer import *
from items import *
from perks import *
from offerings import *
from scores import *
from escape import *
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
        image = image.convert("RGBA")
        canvas = Image.new('RGBA', image.size, (0,0,0,255)) # Empty canvas colour (r,g,b,a)
        canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
        canvas.save(str(location+fileName), format="PNG")

def calculateBrightnessVector(brightness):
    # If brightness is set to 1, then the variable bVector will 135
    fullBrightWhite = 135
    noBrightWhite = 100
    
    difference = fullBrightWhite - noBrightWhite

    bVector = noBrightWhite + (difference * float(brightness))

    return bVector


def addDataToStorage(killerPlayed, perks, items, offerings, scores, escapes, location):
    gameID = 0

    with open(location+'games.json',"r+") as games:
        gameID = 0
        game_data = json.load(games)
        for line in game_data["games"]:
            if line["gameid"] >= gameID:
                gameID = line["gameid"]

        gameID += 1

    # Write Game Data to file

    newGameData = {"gameid":gameID,"date":str(datetime.datetime.now())}
    print(newGameData)

    with open(location+'games.json',"r+") as games:
        game_data = json.load(games)
        game_data["games"].append(newGameData)
        games.seek(0)
        json.dump(game_data, games, indent=4)
    

    # Write Killer Data to file

    newKillerData = {"name":killerPlayed,"gameid":gameID}           
    print(killerPlayed)

    with open(location+'killers.json',"r+") as killers:
        killer_data = json.load(killers)
        killer_data["killers"].append(newKillerData)
        killers.seek(0)
        json.dump(killer_data, killers, indent=4)

    # Write Perk Data to file
    # newPerkData = {"perk":,"gameid":gameID}


    perkArray = []
    for i in perks:
        for j in range(perks[i]):
            perkArray.append(i)
        pass
    
    for i in perkArray:
        newPerkData = {"perk":i,"gameid":gameID}

        with open(location+'perks.json',"r+") as perks:
            perk_data = json.load(perks)
            perk_data["perks"].append(newPerkData)
            perks.seek(0)
            json.dump(perk_data, perks, indent=4)

    itemsArray = []
    for i in items:
        for j in range(items[i]):
            itemsArray.append(i)
        pass

    for i in itemsArray:
        newItemData = {"item":i,"gameid":gameID}
        # print(newItemData)

        with open(location+'items.json',"r+") as items:
            item_data = json.load(items)
            item_data["items"].append(newItemData)
            items.seek(0)
            json.dump(item_data, items, indent=4)
    
    # Write Offering Data to file
    # newOfferingData = {"offering":,"gameid":gameID}

    offeringArray = []
    for i in offerings:
        for j in range(offerings[i]):
            offeringArray.append(i)
        pass

    for i in offeringArray:
        newOfferingData = {"offering":i,"gameid":gameID}

        with open(location+'offerings.json',"r+") as offerings:
            offering_data = json.load(offerings)
            offering_data["offerings"].append(newOfferingData)
            offerings.seek(0)
            json.dump(offering_data, offerings, indent=4)


    print(scores)
    # Write Score Data to file
    newScoreData = {"player1Score": scores["Player1"],"player2Score": scores["Player2"],"player3Score": scores["Player3"],"player4Score": scores["Player4"],"killerScore": scores["Player1"],"gameid":gameID}

    with open(location+'scores.json',"r+") as scores:
        score_data = json.load(scores)
        score_data["scores"].append(newScoreData)
        scores.seek(0)
        json.dump(score_data, scores, indent=4) 

    # Write Escape Data to file
    escapes["gameid"] = gameID

    print(escapes)
    with open(location+'escapes.json',"r+") as escapesFile:
        escape_data = json.load(escapesFile)
        escape_data["escapes"].append(escapes)
        escapesFile.seek(0)
        json.dump(escape_data, escapesFile, indent=4)

    



    


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
        # print(escapes)
        escapes = calculateEscapes(escapeList, "./Escapes/", EscapeScreen)
        print(escapes)
        pass

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
            addDataToStorage(killerPlayed, perks, items, offerings, scores, escapes,"./Outputs/")

    if args.forceEnd:
        cv2.destroyAllWindows()
    else:
        while True:
            key = cv2.waitKey(30)
            if key == 27 or key == 0:
                quit()
    
if __name__ == "__main__":
    main()