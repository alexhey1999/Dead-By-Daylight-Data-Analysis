import os
import re
import cv2
import numpy as np
import pytesseract
from dotenv import load_dotenv,find_dotenv
import random


class Characters:
    def __init__(self, image):
        self.image = image
        self.radius = 18
        self.character_width = 400
        self.character_height = 32
        self.lower_white = 160
        self.crossplay_size = 32
        
        
        if image is not None:
            self.image = self.pre_process_image(image)

        load_dotenv(find_dotenv())
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")
            
    def set_image(self, image):
        self.image = self.pre_process_image(image)
    
    def pre_process_image(self, image):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        WhiteBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        # return image
        return result    
    
    def process_screen(self,image):
        krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        dlt = cv2.dilate(image, krn, iterations=1)
        thr = 255 - cv2.bitwise_and(dlt, image)
        return thr
    
    def find_characters(self,image_to_analyze):
        image_to_analyze = self.process_screen(image_to_analyze)
        text = pytesseract.image_to_string(image_to_analyze,config='--psm 3')
        text = text.strip('\n').strip(".")
        # print(text)
        character = "No Character Found"
        if len(text) > 0:
            try:
                text = text.strip('\n').strip(".") 
                text_endpoint = 3 if "." in str(text).split(" ")[1] else 2
                character = " ".join(str(text).split(" ")[0:text_endpoint]).title()
            except:
                character = "No Character Found"
        else:
            return "No Character Found"
        # print(character.title())
        return character
    
    def compare_characters(self):
        # self.process_screen_image()
        screen = self.image[270:270+self.character_height,180+self.crossplay_size:180+self.crossplay_size+self.character_width]
        # screen = cv2.resize(screen,(self.character_height*5,self.character_width*5))
        cv2.imshow("Crossplay Window",screen)
        
    def run(self,crossplay_dict):
        characters = {}
        
        if crossplay_dict["character_1_crossplay"]:
            characters["player_1"] = self.find_characters(self.image[270:270+self.character_height,180+self.crossplay_size:180+self.crossplay_size+self.character_width])
        else:
            characters["player_1"] = self.find_characters(self.image[270:270+self.character_height,180:180+self.character_width])
        
        if crossplay_dict["character_2_crossplay"]:
            characters["player_2"] = self.find_characters(self.image[388:388+self.character_height,180+self.crossplay_size:180+self.crossplay_size+self.character_width])
        else:
            characters["player_2"] = self.find_characters(self.image[388:388+self.character_height,180:180+self.character_width])
        
        if crossplay_dict["character_3_crossplay"]:
            characters["player_3"] = self.find_characters(self.image[506:506+self.character_height,180+self.crossplay_size:180+self.crossplay_size+self.character_width])
        else:
            characters["player_3"] = self.find_characters(self.image[506:506+self.character_height,180:180+self.character_width])
        
        if crossplay_dict["character_4_crossplay"]:
            characters["player_4"] = self.find_characters(self.image[624:624+self.character_height,180+self.crossplay_size:180+self.crossplay_size+self.character_width])
        else:
            characters["player_4"] = self.find_characters(self.image[624:624+self.character_height,180:180+self.character_width])
            
        return characters
