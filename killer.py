import os
from os import listdir
import cv2
import numpy as np

class Killer:
    def __init__(self, image):
        self.image = image
        self.killer_size = 42
        self.compressed_image = 30
    
    
    def set_image(self, image):
        self.image = image
    
    
    def get_killer_list(self,perk_path):
        return listdir(perk_path)    
    
    def find_best_matching_killer(self,image_to_analyze):
            killer_path = os.getenv('KILLER_LOCATION')
            most_probable_killer = None
            most_probable_killer_score = 0
            for killer in self.get_killer_list(killer_path):
                icon = cv2.imread(f"{killer_path}/{killer}",1)
                icon = cv2.resize(icon,(self.compressed_image,self.compressed_image),interpolation=cv2.INTER_AREA)
                icon = cv2.resize(icon, (self.killer_size, self.killer_size),interpolation=cv2.INTER_AREA)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_killer_score:
                    most_probable_killer_score = maxVal
                    most_probable_killer = killer
                    
            if most_probable_killer:
                return most_probable_killer.split('.')[0]
            else:
                return "No Killer"
        
    def compare_killer(self):
        screen_img = self.image[775:775+self.killer_size,490:490+self.killer_size]
        screen_img = cv2.resize(screen_img,(self.killer_size*5,self.killer_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('KILLER_LOCATION')+'/Demogorgon.png')
        img_file = cv2.resize(img_file,(self.compressed_image,self.compressed_image),interpolation=cv2.INTER_AREA)
        
        img_file = cv2.resize(img_file,(self.killer_size*5,self.killer_size*5))
        cv2.imshow("File Image",img_file)
        
    def run(self):
        # Killer Analysis
        killer = self.find_best_matching_killer(self.image[775:775+self.killer_size,490:490+self.killer_size])
        return killer