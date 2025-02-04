import os
from os import listdir
import cv2
import numpy as np
import pytesseract
from dotenv import load_dotenv,find_dotenv


class Scores:
    def __init__(self, image, lower_white = None):
        self.lower_white_default = 170
        self.image = image
        self.radius = 18
        self.score_width = 150
        # self.score_height = 550
        self.score_height = 60
        self.lower_white = 170
        
        if image is not None:
            self.image = self.pre_process_image(image)
        
        # Assign Pytesseract path for text processing functions
        load_dotenv(find_dotenv())
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")
            
    def set_image(self, image):
        self.image = self.pre_process_image(image)
    
    def set_lower_white(self, image_lower_white = None,image = None):
        if image_lower_white is None:
            self.lower_white = int(self.lower_white_default)
        else:
            self.lower_white = int(image_lower_white * 1.5)
            self.image = self.pre_process_image(image)
            self.lower_white = int(self.lower_white_default)
    
    def pre_process_image(self, image):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        WhiteBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        return result
        
    
    def process_screen(self,image):
        krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        dlt = cv2.dilate(image, krn, iterations=1)
        thr = 255 - cv2.bitwise_and(dlt, image)
        return thr
    
    def find_scores(self,image_to_analyze):
        # text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        image_to_analyze = self.process_screen(image_to_analyze)
        text = pytesseract.image_to_string(image_to_analyze,config='--psm 10')
        # print(f'Text Extrapolated: \n{text}')
        text = text.replace('.','').replace(' ','').split('\n')
        text = [i for i in text if i]
        
        # print(f'Text Extrapolated: \n{text}')
        
        score = 0
        try:
            score = int(text[0])
        except:
            score = "NAN"
        
        return score
    
    def compare_scores(self):
        # self.process_screen_image()
        screen_perk = self.image[540:540+self.score_height,720:720+self.score_width]
        screen_perk = self.process_screen(screen_perk)
        cv2.imshow("Score Window",screen_perk)
        
    def run(self):
        scores = {}
        scores["player_1"] = self.find_scores(self.image[300:300+self.score_height,720:720+self.score_width])
        scores["player_2"] = self.find_scores(self.image[420:420+self.score_height,720:720+self.score_width])
        scores["player_3"] = self.find_scores(self.image[540:540+self.score_height,720:720+self.score_width])
        scores["player_4"] = self.find_scores(self.image[660:660+self.score_height,720:720+self.score_width])
        scores["killer"] = self.find_scores(self.image[775:775+self.score_height,720:720+self.score_width])
        
        # print(scores)
        return scores