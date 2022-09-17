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
from screen_capping import Screen
import os
from dotenv import load_dotenv,find_dotenv
from screeninfo import get_monitors

# Import Analyser Classes
from perks import Perks
from killer import Killer
from offerings import Offerings


def main():
    # image, filename = ScreenTaker.get_image_capture()
    # print("Image Taken")
    
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_full.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_1.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_mori.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_difficult_survivor_perks.png')
    image, filename = ScreenTaker.get_image_from_filename('./Tests/test_disconnected.png')
    
    image = ScreenTaker.process_screen_image(image)
    
    PerkAnalyser = Perks(image)
    KillerAnalyser = Killer(image)
    OfferingAnalyser = Offerings(image)
    
    # ScreenTaker.show_image(image[660:660+55,420:420+55],'Display')
    ScreenTaker.show_image(image,'Display')
    
    
    #Offering Tests 
    
    # OfferingAnalyser.compare_offering()
    offerings = OfferingAnalyser.run()
    print("Offerings: ", offerings)
    
    
    
    
    # killer = KillerAnalyser.run()
    # print("Killer: ",killer)

    # survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    # print("Survivor Perks Used: " + str(survivor_perks_used))
    # print("Killer Perks Used: " + str(killer_perks_used))
    
    
    while True:
        key = cv2.waitKey(30)
        if key == 27 or key == 0:
            quit()
    
    
    
if __name__ == "__main__":
    # Load .env file
    load_dotenv(find_dotenv())
    
    # Assign Pytesseract path for text processing functions
    pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")

    # Create Screen Capture Object
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]

    ScreenTaker = Screen(monitor.width, monitor.height)
    
    
    # Calculate BVector value
    brightness_vector = ScreenTaker.calculate_brightness_vector(1)
    
    main()