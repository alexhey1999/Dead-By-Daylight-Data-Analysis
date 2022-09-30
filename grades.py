import os
from os import listdir
import cv2
import numpy as np
import pytesseract
from dotenv import load_dotenv,find_dotenv


class Grades:
    def __init__(self, image):
        self.image = image
        self.lower_white_default = 170
        self.grade_width = 70
        self.grade_height = 50
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
            self.lower_white = int(image_lower_white * 1.46)
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
        # return image
        
    
    def process_screen(self,image):
        krn = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 3))
        dlt = cv2.dilate(image, krn, iterations=1)
        thr = 255 - cv2.bitwise_and(dlt, image)
        return thr
    
    def find_grades(self,image_to_analyze):
        # text = pytesseract.image_to_string(Screen, lang='eng',config='--psm 6 --oem 3 -c tessedit_char_whitelist=0123456789')
        image_to_analyze = self.process_screen(image_to_analyze)
        text = pytesseract.image_to_string(image_to_analyze,config='--psm 10')
        # print(f'Text Extrapolated: \n{text}')
        text = text.replace('.','').replace(' ','').split('\n')
        text = [i for i in text if i]
        
        # print(f'Text Extrapolated: \n{text}')
        
        grade = 0
        try:
            grade = int(text[0])
        except:
            grade = "NAN"
        
        return grade
    
    def compare_grades(self):
        # self.process_screen_image()
        screen_perk = self.image[750:750+self.grade_height,92:92+self.grade_width]
        # screen_perk = self.process_screen(screen_perk)
        cv2.imshow("Grade Window",screen_perk)
        
    def run(self):
        grades = {}
        grades["player_1"] = self.find_grades(self.image[286:286+self.grade_height,92:92+self.grade_width])
        grades["player_2"] = self.find_grades(self.image[405:405+self.grade_height,92:92+self.grade_width])
        grades["player_3"] = self.find_grades(self.image[522:522+self.grade_height,92:92+self.grade_width])
        grades["player_4"] = self.find_grades(self.image[640:640+self.grade_height,92:92+self.grade_width])
        grades["killer"] = self.find_grades(self.image[750:750+self.grade_height,92:92+self.grade_width])
        
        # print(scores)
        return grades