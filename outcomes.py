import os
from os import listdir
from subprocess import CREATE_NEW_PROCESS_GROUP
import cv2
import numpy as np
import random

class Outcomes:
    def __init__(self, image):
        self.image = image
        self.outcome_height = 86
        self.outcome_width = 80
        self.lower_white = 130

    def set_image(self, image):
        self.image = image
    
    
    def get_outcome_list(self,perk_path):
        return listdir(perk_path)
    
    
    def file_outcome_processing(self,image,height,width):
        upper_white = np.array([255, 255, 255])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        image = cv2.bitwise_and(image, image, mask = mask)
        image = cv2.resize(image, (width,height),interpolation=cv2.INTER_AREA)
        return image
    
    def screen_image_processing(self,image):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        WhiteBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        self.image = result
        
    def find_best_matching_outcome(self,image_to_analyze):
        outcome_path = os.getenv('OUTCOME_LOCATION')
        outcomes = {}
        height, width, threshold, name = 0, 0, 0.8, "None"
        for outcome in self.get_outcome_list(outcome_path):
            if outcome == "alive.png":
                height, width, threshold, name = (48,40,0.8,"Alive")
            if outcome == "death.png":
                height, width, threshold, name = (45,38,0.75,"Death")
            if outcome == "disconnected.png":
                height, width, threshold, name = (35,52,0.75,"Disconnected")
            if outcome == "escape.png":
                height, width, threshold, name = (40,35,0.75, "Escape")
            if outcome == "sacrificed.png":
                height, width, threshold, name = (57,40,0.75, "Sacrificed")
            
            icon = cv2.imread(f"{outcome_path}/{outcome}",1)
            icon = self.file_outcome_processing(icon, height, width)
            result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCORR_NORMED)
            yloc, xloc = np.where(result >= threshold)
            rectangles = []

            for (x, y) in zip(xloc, yloc):
                rectangles.append([int(x), int(y), width,height])
                rectangles.append([int(x), int(y), width,height])

            rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.2)
            
            color = tuple(list(np.random.choice(range(256), size=3)))

            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            for (x, y, w, h) in rectangles:
                cv2.putText(image_to_analyze, outcome, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, color, 1)
                cv2.rectangle(image_to_analyze, (x, y), (x + w, y + h), color, 2)

            if len(rectangles) > 0:
                return outcome.split('.')[0]
        
        

        return "No Outcome"
    
    
    def compare_outcomes(self):
        screen_img = self.image[780:780+self.outcome_size,422:422+self.outcome_size]
        screen_img = cv2.resize(screen_img,(self.outcome_size*5,self.outcome_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('OUTCOME_LOCATION')+'/disconnected.png')
        img_file = cv2.resize(img_file,(self.outcome_size*5,self.outcome_size*5))
        cv2.imshow("File Image",img_file)
        
    
    
    def run(self):
        # cv2.imshow("Screen",self.image[290:290+self.outcome_height,890:890+self.outcome_width])
        cv2.imshow("Screen",self.image[752:752+self.outcome_height,890:890+self.outcome_width])
        self.screen_image_processing(self.image)
        # outcomes = None
        # self.find_best_matching_outcome(self.image[290:290+self.outcome_height,890:890+self.outcome_width])
        
        player_1_outcome = self.find_best_matching_outcome(self.image[290:290+self.outcome_height,890:890+self.outcome_width])
        player_2_outcome = self.find_best_matching_outcome(self.image[410:410+self.outcome_height,890:890+self.outcome_width])
        player_3_outcome = self.find_best_matching_outcome(self.image[525:525+self.outcome_height,890:890+self.outcome_width])
        player_4_outcome = self.find_best_matching_outcome(self.image[642:642+self.outcome_height,890:890+self.outcome_width])
        killer_outcome = self.find_best_matching_outcome(self.image[754:754+self.outcome_height,890:890+self.outcome_width])
        
        return player_1_outcome, player_2_outcome, player_3_outcome, player_4_outcome, killer_outcome
        