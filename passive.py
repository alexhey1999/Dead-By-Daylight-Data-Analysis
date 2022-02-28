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
import time

path = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# path = r'C:\Users\alex.hey\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

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


def addDataToStorage(killerPlayed, perks, items, offerings, scores, escapes, location,file):
    gameID = 0

    try:
        newScoreData = {"player1Score": scores["Player1"],"player2Score": scores["Player2"],"player3Score": scores["Player3"],"player4Score": scores["Player4"],"killerScore": scores["Killer"],"gameid":gameID}
    except:
        print("Invalid Score Data")
        return

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
    newScoreData = {"player1Score": scores["Player1"],"player2Score": scores["Player2"],"player3Score": scores["Player3"],"player4Score": scores["Player4"],"killerScore": scores["Killer"],"gameid":gameID}

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

    rename(file, "Screenshots/Archived/"+file.split('/')[1])



    


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

    if args.brightness:
        bVector = int(calculateBrightnessVector(args.brightness))
    else:
        bVector = int(calculateBrightnessVector(1))
    
    # set output file
    killerList = listdir("./Killers/")
    perkList = listdir("./Perks/")
    itemList = listdir("./Items/")
    offeringList = listdir("./Offerings/")
    escapeList = listdir("./Escapes/")

    print("Starting Search...")
    while True:
        img = ImageGrab.grab(bbox=(70, 100, 350, 170)) #x, y, w, h
        img_np = np.array(img)
        screen = cv2.cvtColor(img_np, cv2.COLOR_BGR2HSV)
        
        lowerRed  = np.array([100,100,100])
        upperRed= np.array([255,255,255])

        mask = cv2.inRange(screen, lowerRed, upperRed)
        WhiteBackground = np.zeros((screen.shape[0], screen.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)

        BlackBackground = np.zeros((screen.shape[0], screen.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)

        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        
        result = cv2.bitwise_not(result)

        text = pytesseract.image_to_string(result, lang='eng',config='--psm 6')
        # print(text)
        if "SCOREBOARD" in str(text) :
            print("Scoreboard Found - Saving Data")
            time.sleep(2)
            screenshotName = getImageCapture()

            KillerScreen = cv2.imread('Screenshots/'+screenshotName)
            PerkScreen = cv2.imread('Screenshots/'+screenshotName)
            ItemScreen = cv2.imread('Screenshots/'+screenshotName)
            OfferingScreen = cv2.imread('Screenshots/'+screenshotName)
            ScoreScreen = cv2.imread('Screenshots/'+screenshotName)
            EscapeScreen = cv2.imread('Screenshots/'+screenshotName)

            imgFile = "Screenshots/"+screenshotName

            KillerScreen = adjustScreenSizeKiller(KillerScreen, bVector)
            PerkScreen = adjustScreenSizePerks(PerkScreen, bVector)
            ItemScreen = adjustScreenSizeItems(ItemScreen, bVector)
            OfferingScreen = adjustScreenSizeOfferings(OfferingScreen, bVector)
            ScoreScreen = adjustScreenSizeScores(ScoreScreen, bVector)
            EscapeScreen = adjustScreenSizeEscapes(EscapeScreen, bVector)
            
            killerPlayed, confirmation = calculateKiller(killerList, "./Killers/", KillerScreen,False)
            perks = calculatePerks(perkList, "./Perks/", PerkScreen,False)
            items = calculateItems(itemList, "./Items/", ItemScreen,False)
            offerings = calculateOfferings(offeringList, "./Offerings/", OfferingScreen,False)
            scores = calculateScores(ScoreScreen,False)
            escapes = calculateEscapes(escapeList, "./Escapes/", EscapeScreen,bVector,False)

            print('\n\n\n\n\n\n')
            print(f'Killer Played: {killerPlayed} , Confirmation: {round(confirmation*100,2)}%\n')
            print(f'Perks: {perks}\n')
            print(f'Items: {items}\n')
            print(f'Offerings: {offerings}\n')
            print(f'Scores: {scores}\n')
            print(f'Escapes: {escapes}\n')

            # print(escapes["escape"])
            if "alive" in escapes:
                print("Game Still In Progress")
                continue
            addDataToStorage(killerPlayed, perks, items, offerings, scores, escapes,"./Outputs/", imgFile)
            print("Starting look for new game")
            while True:
                img = ImageGrab.grab(bbox=(115, 990, 180, 1020)) #x, y, w, h
                img_np = np.array(img)
                screen = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)
                
                lowerRed  = np.array([100,100,100])
                upperRed= np.array([255,255,255])

                mask = cv2.inRange(screen, lowerRed, upperRed)
                WhiteBackground = np.zeros((screen.shape[0], screen.shape[1], 3), dtype=np.uint8)
                WhiteBackground[:,:,:] = (255,255,255)

                BlackBackground = np.zeros((screen.shape[0], screen.shape[1], 3), dtype=np.uint8)
                BlackBackground[:,:,:] = (0,0,0)

                result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
                
                screen = cv2.bitwise_not(result)

                text = pytesseract.image_to_string(result, lang='eng',config='--psm 6')
                if "BACK" in text:
                    print("Back Button Found - Restarting Search for Scoreboard")
                    break
    
if __name__ == "__main__":
    main()