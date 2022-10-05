import uuid
import pyautogui
import numpy as np
import PIL.Image as Image
import cv2
import time
from dotenv import load_dotenv,find_dotenv
import pytesseract
import os
import re

from killer import Killer


class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lower_white = 105
        self.brightness_scalar = 3.7
        self.screenshot_interval = 0.5  # seconds
        
        self.score_width = 90
        self.score_height = 35
        
        self.back_width = 60
        self.back_height = 27

        load_dotenv(find_dotenv())
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")
        
    def calculate_and_set_brightness_vector(self,image):
        image = Image.fromarray(image)
        greyscale_image = image.convert('L')
        histogram = greyscale_image.histogram()
        pixels = sum(histogram)
        brightness = scale = len(histogram)

        for index in range(0, scale):
            ratio = histogram[index] / pixels
            brightness += ratio * (-scale + index)

        brightness_value = 1 if brightness == 255 else brightness / scale
        lower_white_calculation = (brightness_value * self.brightness_scalar) * self.lower_white
        self.lower_white = round(lower_white_calculation)
        return(self.lower_white)
    
    def get_image_capture(self):
        fileName = f'{str(uuid.uuid4())}.png'
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        # cv2.imwrite('processing/'+fileName, image)
        return image, fileName

    def get_image_from_filename(self, filename):
        image_id = filename.split('/')[-1]
        image = cv2.imread(filename)
        # image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        return image, filename
    
    def process_screen_image(self,image):
        self.calculate_and_set_brightness_vector(image)
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        WhiteBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        return result
    
    def endgame_identifier_image_process(self, image):
        image = image[218:218+self.score_height,788:788+self.score_width]
        # image = cv2.bitwise_not(image)
        return image
        
    def lobby_identifier_image_process(self, image):
        image = image[991:991+self.back_height,115:115+self.back_width]
        image = cv2.bitwise_not(image)
        return image
    
    def save_image(self, image, name):
        screenshot_path = os.getenv("SCREENSHOT_LOCATIONS")
        cv2.imwrite(f"{screenshot_path}/{name}",image)
        return f"{screenshot_path}/{name}"
    
    def test_endscreen(self):     
        while True:
            time.sleep(self.screenshot_interval)
            image, filename = self.get_image_capture()
            ident_img = self.endgame_identifier_image_process(image)
            try:
                text = pytesseract.image_to_string(ident_img)
                text = re.sub(r'[^a-zA-Z]', '', text)
                if text == "SCORE":
                    time.sleep(1)
                    image, filename = self.get_image_capture()
                    
                    killerAnalyser = Killer(image)
                    killer = killerAnalyser.run()
                    if killer == "No Killer":
                        continue                    
                    
                    filename = self.save_image(image, filename)
                    return image, filename
            except:
                continue
    
    def test_lobby(self):
        while True:
            time.sleep(self.screenshot_interval)
            image, filename = self.get_image_capture()
            ident_img = self.lobby_identifier_image_process(image)
            try:
                text = pytesseract.image_to_string(ident_img)
                text = re.sub(r'[^a-zA-Z]', '', text)
                if text == "BACK":
                    return True
            except:
                continue
    
    def show_image(self, image,name="No Name Given"):
        cv2.imshow(name,image)