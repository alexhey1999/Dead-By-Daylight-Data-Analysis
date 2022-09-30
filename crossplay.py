import os
import re
import cv2
import numpy as np
import pytesseract
from dotenv import load_dotenv,find_dotenv
import random


class Crossplay:
    def __init__(self, image):
        self.image = image
        self.lower_white_default = 170
        self.radius = 18
        self.lower_white = 160
        self.crossplay_size = 22
        self.crossplay_threshold = 0.6
        
        if image is not None:
            self.image = self.pre_process_image(image)

        load_dotenv(find_dotenv())
        pytesseract.pytesseract.tesseract_cmd = os.getenv("PYTESSERACT_PATH")
        
    def set_lower_white(self, image_lower_white = None,image = None):
        if image_lower_white is None:
            self.lower_white = int(self.lower_white_default)
        else:
            self.lower_white = int(image_lower_white * 1.46)
            self.image = self.pre_process_image(image)
            self.lower_white = int(self.lower_white_default)
            
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
        return result
    
    def crossplay_file_processing(self,icon):
        icon = cv2.resize(icon, (self.crossplay_size, self.crossplay_size),interpolation=cv2.INTER_AREA)
        mask = np.zeros((self.crossplay_size, self.crossplay_size), np.uint8)
        circle_img = cv2.circle(mask,(int(self.crossplay_size/2),int(self.crossplay_size/2)),self.radius,(255,255,255),thickness=-1)
        icon = cv2.bitwise_and(icon, icon, mask=circle_img)
        return icon
    
    def determine_crossplay(self,image_to_analyze):
        outcome_path = os.getenv('HELP_LOCATION')
        crossplay_file_name = "Crossplay.png"
        icon = cv2.imread(f"{outcome_path}/{crossplay_file_name}",1)
        icon = self.crossplay_file_processing(icon)
        result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCORR_NORMED)
        yloc, xloc = np.where(result >= self.crossplay_threshold)
        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), self.crossplay_size,self.crossplay_size])
            rectangles.append([int(x), int(y), self.crossplay_size,self.crossplay_size])
        rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.2)
        color = tuple(list(np.random.choice(range(256), size=3)))
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        for (x, y, w, h) in rectangles:
            cv2.putText(image_to_analyze, crossplay_file_name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
            cv2.rectangle(image_to_analyze, (x, y), (x + w, y + h), color, 2)

        if len(rectangles) > 0:
            return True
        return False
    
    def compare_crossplay(self):
        # self.process_screen_image()
        screen = self.image[743:743+self.crossplay_size,192:192+self.crossplay_size]
        screen = cv2.resize(screen,(self.crossplay_size*5,self.crossplay_size*5))
        # screen = self.process_screen(screen)
        outcome_path = os.getenv('HELP_LOCATION')
        icon = cv2.imread(f"{outcome_path}/Crossplay.png",1)
        
        icon = self.crossplay_file_processing(icon)
        icon = cv2.resize(icon,(self.crossplay_size*5,self.crossplay_size*5))
        
        cv2.imshow("Crossplay Window",screen)
        cv2.imshow("Crossplay File",icon)
        
    def run(self):
        crossplay = {}
        
        crossplay["character_1_crossplay"] = self.determine_crossplay(self.image[279:279+self.crossplay_size,192:192+self.crossplay_size])
        crossplay["character_2_crossplay"] = self.determine_crossplay(self.image[396:396+self.crossplay_size,192:192+self.crossplay_size])
        crossplay["character_3_crossplay"] = self.determine_crossplay(self.image[513:513+self.crossplay_size,192:192+self.crossplay_size])
        crossplay["character_4_crossplay"] = self.determine_crossplay(self.image[631:631+self.crossplay_size,192:192+self.crossplay_size])
        crossplay["killer_crossplay"] = self.determine_crossplay(self.image[743:743+self.crossplay_size,192:192+self.crossplay_size])

        return crossplay
