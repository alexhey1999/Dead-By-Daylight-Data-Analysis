import os
from os import listdir
import cv2
import numpy as np

class Killer:
    def __init__(self, image):
        self.image = image
        self.perk_size = 50
        self.lower_white = 100
    
    
    def set_image(self, image):
        self.image = image
    
    
    def get_killer_list(self,perk_path):
        return listdir(perk_path)
    
    
    def show_screen(self):
        cv2.imshow("Perk Screen ", self.image)
    
        
    def show_image(self, image,name="No Name Given"):
        cv2.imshow(name,image)
    
    
    def find_best_matching_killer(self,image_to_analyze):
            killer_path = os.getenv('KILLER_LOCATION')
            most_probable_killer = None
            most_probable_killer_score = 0
            for killer in self.get_killer_list(killer_path):
                icon = cv2.imread(f"{killer_path}/{killer}",1)   
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_killer_score:
                    most_probable_killer_score = maxVal
                    most_probable_killer = killer
                    
            if most_probable_killer:
                return most_probable_killer.split('.')[0]
            else:
                return "No Perk"
    
    
        
    def run(self):
        # Player 1
        player_1_perk_1 = self.find_best_matching_killer(self.image[310:310+self.perk_size,193:193+self.perk_size])))     
        
        return survivor_perks_used, killer_perks_used