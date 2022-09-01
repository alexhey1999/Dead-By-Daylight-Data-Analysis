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


def main():
    # image, filename = ScreenTaker.get_image_capture()
    # print("Image Taken")
    
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_full.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_disconnected.png')
    # image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_1.png')
    image, filename = ScreenTaker.get_image_from_filename('./Tests/test_mori.png')
    
    PerkAnalyser = Perks(image,None)
    # PerkAnalyser.test_perk_loaded()
    PerkAnalyser.size_comparison()
    
    # while True:pass
    PerkAnalyser.show_screen()
    survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    # print(survivor_perks_used)
    print("Survivor Perks Used: " + ', '.join(survivor_perks_used))
    print("Killer Perks Used: " + ', '.join(killer_perks_used))
    
    
    # PerkAnalyser.perk_test()
    
    
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