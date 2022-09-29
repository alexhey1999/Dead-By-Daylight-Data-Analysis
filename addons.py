import os
from os import listdir
import cv2
import numpy as np

class Addons:
    def __init__(self, image):
        self.image = image
        self.addon_size = 35
        self.compressed_image = 30
        self.radius = 17
        self.threshold = 0.6
    
    
    def set_image(self, image):
        self.image = image
    
    def get_addon_list(self,perk_path):
        return listdir(perk_path)    
    
    def find_best_matching_addon(self,image_to_analyze,killer = None):
            addon_path = os.getenv('ADDON_LOCATION')
            image_to_analyze = self.addon_image_processing(image_to_analyze)
            if killer == None:
                addon_path = addon_path + "/Survivor"
            else:
                addon_path = addon_path + "/" + killer
            most_probable_addon = None
            most_probable_addon_score = 0
            for addon in self.get_addon_list(addon_path):
                icon = cv2.imread(f"{addon_path}/{addon}",1)
                icon = self.addon_file_processing(icon)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_addon_score and maxVal >= self.threshold:
                    most_probable_addon_score = maxVal
                    most_probable_addon = addon
                    
            if most_probable_addon:
                return most_probable_addon.split('.')[0]
            else:
                return "No Addon"
            
    def addon_image_processing(self,icon):
        # cv2.cvtColor(icon, cv2.COLOR_HSV2BGR)
        icon = cv2.resize(icon, (self.addon_size,self.addon_size),interpolation=cv2.INTER_AREA)
        mask = np.zeros((self.addon_size,self.addon_size), np.uint8)
        circle_img = cv2.circle(mask,(int(self.addon_size/2),int(self.addon_size/2)),self.radius,(255,255,255),thickness=-1)
        icon = cv2.bitwise_and(icon, icon, mask=circle_img)
        return icon
        
    def addon_file_processing(self,icon):
        # cv2.cvtColor(icon, cv2.COLOR_HSV2BGR)
        icon = cv2.resize(icon,(self.compressed_image,self.compressed_image),interpolation=cv2.INTER_AREA)
        icon = cv2.resize(icon, (self.addon_size,self.addon_size),interpolation=cv2.INTER_AREA)
        mask = np.zeros((self.addon_size,self.addon_size), np.uint8)
        circle_img = cv2.circle(mask,(int(self.addon_size/2),int(self.addon_size/2)),self.radius,(255,255,255),thickness=-1)
        icon = cv2.bitwise_and(icon, icon, mask=circle_img)
        return icon
    
    def compare_addons(self):
        screen_img = self.image[670:670+self.addon_size,595:595+self.addon_size]
        print(screen_img.shape)
        # screen_img = self.addon_image_processing(screen_img)
        screen_img = cv2.resize(screen_img, (self.addon_size*5, self.addon_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('ADDON_LOCATION')+'/Demogorgon/Barbs Glasses.png')
        img_file = cv2.resize(img_file,(self.compressed_image,self.compressed_image),interpolation=cv2.INTER_AREA)
        img_file = self.addon_image_processing(img_file)
        print(img_file.shape)
        cv2.imshow("File Image",img_file)
        
    def run(self, killer = None):
        addons = {}
        # Survivor 1 Addons
        addons["player_1"] = {}
        addons["player_1"]["addon_1"] = self.find_best_matching_addon(self.image[318:318+self.addon_size,554:554+self.addon_size])
        addons["player_1"]["addon_2"] = self.find_best_matching_addon(self.image[318:318+self.addon_size,595:595+self.addon_size])
        
        # Survivor 2 Addons
        addons["player_2"] = {}
        addons["player_2"]["addon_1"] = self.find_best_matching_addon(self.image[435:435+self.addon_size,554:554+self.addon_size])
        addons["player_2"]["addon_2"] = self.find_best_matching_addon(self.image[435:435+self.addon_size,595:595+self.addon_size])
        
        # Survivor 3 Addons
        addons["player_3"] = {}
        addons["player_3"]["addon_1"] = self.find_best_matching_addon(self.image[552:552+self.addon_size,554:554+self.addon_size])
        addons["player_3"]["addon_2"] = self.find_best_matching_addon(self.image[552:552+self.addon_size,595:595+self.addon_size])
        
        # Survivor 4 Addons
        addons["player_4"] = {}
        addons["player_4"]["addon_1"] = self.find_best_matching_addon(self.image[670:670+self.addon_size,554:554+self.addon_size])
        addons["player_4"]["addon_2"] = self.find_best_matching_addon(self.image[670:670+self.addon_size,595:595+self.addon_size])
        # Killer Addons
        addons["killer"] = {}
        addons["killer"]["addon_1"] = self.find_best_matching_addon(self.image[777:777+self.addon_size,552:552+self.addon_size],killer)
        addons["killer"]["addon_2"] = self.find_best_matching_addon(self.image[777:777+self.addon_size,593:593+self.addon_size],killer)
        
        return addons