#Handle Imports
from msilib.schema import File
import cv2
import sys
from os import listdir, rename
import argparse
import pyautogui
import numpy as np
import pytesseract
import PIL.Image as Image
from PIL import ImageGrab
import json
import datetime
from screen_capping import Screen
import os
from dotenv import load_dotenv,find_dotenv
from screeninfo import get_monitors

# Import Analyser Classes
from perks import Perks
from killer import Killer
from offerings import Offerings
from items import Items
from scores import Scores
from outcomes import Outcomes
from grades import Grades
from crossplay import Crossplay
from characters import Characters
from addons import Addons
from database_handling import Database

image = None
    
def main(image, filename, show_images = None):
    # global image
    show_images = True if show_images == None else False
    
    pre_processed_image = image
    
    image = ScreenTaker.process_screen_image(image)
    
    PerkAnalyser = Perks(image)
    KillerAnalyser = Killer(image)
    OfferingAnalyser = Offerings(image)
    ItemAnalyser = Items(image)
    AddonAnalyser = Addons(image)
    OutcomeAnalyser = Outcomes(image)
    
    GradeAnalyser = Grades(pre_processed_image)
    ScoreAnalyser = Scores(pre_processed_image)
    CrossplayAnalyser = Crossplay(pre_processed_image)
    CharacterAnalyser = Characters(pre_processed_image)
    DatabaseHandler = Database()
    
    ScoreAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    GradeAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    CrossplayAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    CharacterAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)

    killer = KillerAnalyser.run()
    survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    items_used = ItemAnalyser.run()
    scores = ScoreAnalyser.run()
    outcomes = OutcomeAnalyser.run()
    offerings = OfferingAnalyser.run()
    grades = GradeAnalyser.run()
    crossplay = CrossplayAnalyser.run()
    characters = CharacterAnalyser.run(crossplay)
    addons = AddonAnalyser.run(killer)
    
    print(killer_perks_used)
    
    # DatabaseHandler.store_data(
    #     filename,
    #     killer,
    #     survivor_perks_used,
    #     killer_perks_used,
    #     items_used,
    #     scores,
    #     outcomes,
    #     offerings,
    #     grades,
    #     crossplay,
    #     characters,
    #     addons
    #     )
        
    while show_images:
        ScreenTaker.show_image(pre_processed_image,'image')
        key = cv2.waitKey(30)
        if key == 27 or key == 0:
            quit()
    
    
if __name__ == "__main__":
    # print(sys.argv)
    show_images = None
    if len(sys.argv) == 2:
        show_images = True if sys.argv[1] == True else False
    
    # Load .env file
    load_dotenv(find_dotenv())

    # Create Screen Capture Object
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]

    ScreenTaker = Screen(monitor.width, monitor.height)
    
    while True:
        print("==========================")
        print("Looking for endgame screen")
        print("==========================")
        image, filename = ScreenTaker.test_endscreen()
        print("Endgame Screen Found!")
        print("==========================")
        main(image, filename, True)
        print("Looking for Lobby Screen")
        print("==========================")
        ScreenTaker.test_lobby()
        print("Lobby Screen Found!")
        