import os
from os import listdir
import cv2
import numpy as np

class Items:
    def __init__(self, image):
        self.image = image
        self.item_size = 38
    
    
    def set_image(self, image):
        self.image = image
    
    
    def get_item_list(self,item_path):
        return listdir(item_path)    
    
    def find_best_matching_item(self,image_to_analyze):
            item_path = os.getenv('ITEM_LOCATION')
            most_probable_item = None
            most_probable_item_score = 0
            for item in self.get_item_list(item_path):
                icon = cv2.imread(f"{item_path}/{item}",1)
                icon = cv2.resize(icon, (self.item_size, self.item_size),interpolation=cv2.INTER_AREA)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_item_score:
                    most_probable_item_score = maxVal
                    most_probable_item = item
                    
            if most_probable_item:
                return most_probable_item.split('.')[0]
            else:
                return "No Item"
        
    def compare_item(self):
        screen_img = self.image[553:553+self.item_size,492:492+self.item_size]
        screen_img = cv2.resize(screen_img,(self.item_size*5,self.item_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('ITEM_LOCATION')+'/Rainbow Map.png')
        img_file = cv2.resize(img_file,(self.item_size*5,self.item_size*5))
        cv2.imshow("File Image",img_file)
        
    def run(self):
        items = {}
        # Item Anal     
        items["player_1"] = self.find_best_matching_item(self.image[317:317+self.item_size,492:492+self.item_size])

        # # Player 2
        items["player_2"] = self.find_best_matching_item(self.image[435:435+self.item_size,492:492+self.item_size])
        
        # # Player 3
        items["player_3"] = self.find_best_matching_item(self.image[553:553+self.item_size,492:492+self.item_size])
        
        # # Player 4
        items["player_4"] = self.find_best_matching_item(self.image[671:671+self.item_size,492:492+self.item_size])
        
        return items