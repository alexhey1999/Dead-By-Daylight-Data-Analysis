#Handle Imports
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

def brighness_calculation(image):
    greyscale_image = image.convert('L')
    histogram = greyscale_image.histogram()
    pixels = sum(histogram)
    brightness = scale = len(histogram)

    for index in range(0, scale):
        ratio = histogram[index] / pixels
        brightness += ratio * (-scale + index)

    return 1 if brightness == 255 else brightness / scale
    
    
def main(show_images = None):
    show_images = True if show_images == None else False
    # print(show_images)
    # show_images = True if show_images == None else False
    # image, filename = ScreenTaker.get_image_capture()
    # print("Image Taken")
    
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_full.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_1.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_mori.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_difficult_survivor_perks.png')
    image, filename = ScreenTaker.get_image_from_filename('./Tests/test_disconnected.png')
    
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_2.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_3.png')
    ScreenTaker.show_image(image,'Display')
    
    image = ScreenTaker.process_screen_image(image)    
    
    PerkAnalyser = Perks(image)
    KillerAnalyser = Killer(image)
    OfferingAnalyser = Offerings(image)
    ItemAnalyser = Items(image)
    
    # OfferingAnalyser.compare_offering()
    # offerings = OfferingAnalyser.run()
    # print("Offerings: ", offerings)    
    
    # KillerAnalyser.compare_killer()
    # killer = KillerAnalyser.run()
    # print("Killer: ",killer)

    # PerkAnalyser.compare_perk()
    # survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    # print("Survivor Perks Used: " + str(survivor_perks_used))
    # print("Killer Perks Used: " + str(killer_perks_used))
    
    ItemAnalyser.compare_item()
    items_used = ItemAnalyser.run()
    print("Items Used: " + str(items_used))
    
    
    
    # ScreenTaker.show_image(image,'Display')
    
    while show_images:
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
    
    # Assign Pytesseract path for text processing functions
    pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")

    # Create Screen Capture Object
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]

    ScreenTaker = Screen(monitor.width, monitor.height)
    
    main(show_images)