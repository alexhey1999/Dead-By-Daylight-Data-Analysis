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
    
def main(show_images = None):
    global image
    show_images = True if show_images == None else False
    # print(show_images)
    # show_images = True if show_images == None else False
    # image, filename = ScreenTaker.get_image_capture()
    # print("Image Taken")
    
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_full.png')
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_1.png')
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_mori.png')
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_difficult_survivor_perks.png')
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_disconnected.png')
    image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_crossplay.png')
    
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_2.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_3.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_4.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_5.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_6.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_7.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_8.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_9.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_10.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_11.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_12.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_13.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_14.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_15.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_16.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_17.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_18.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_19.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_20.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_22.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_23.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_24.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_25.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_26.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_27.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_28.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_29.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_random_30.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_skerm.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Screenshots/test_alive.png')

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
    
    DatabaseHandler.store_data(
        filename,

        
        )
    
        
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
    
    main(show_images)