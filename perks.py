import os
from os import listdir
import cv2
import numpy as np

class Perks:
    def __init__(self, image):
        self.image = image
        self.perk_size = 50
        self.radius = 18
    
    def set_image(self, image):
        self.image = image
    
    def get_perk_list(self,perk_path):
        return listdir(perk_path) 
    
    def find_best_matching_perk(self,image_to_analyze, survivor = True):
            image_to_analyze = self.perk_file_processing(image_to_analyze)   
        
            if survivor:
                perk_path = os.getenv('PERK_LOCATION_SURVIVOR')
            else:
                perk_path = os.getenv('PERK_LOCATION_KILLER')
                
            most_probable_perk = None
            most_probable_perk_score = 0
            for perk in self.get_perk_list(perk_path):
                icon = cv2.imread(f"{perk_path}/{perk}",1)
                icon = self.perk_file_processing(icon)          
                
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                # result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_SQDIFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_perk_score:
                    most_probable_perk_score = maxVal
                    most_probable_perk = perk
                    
            if most_probable_perk:
                return most_probable_perk.split('.')[0]
            else:
                return "No Perk"
    
    def perk_file_processing(self,icon):
        # cv2.cvtColor(icon, cv2.COLOR_HSV2BGR)
        icon = cv2.resize(icon, (self.perk_size, self.perk_size),interpolation=cv2.INTER_AREA)
        mask = np.zeros((self.perk_size, self.perk_size), np.uint8)
        circle_img = cv2.circle(mask,(int(self.perk_size/2),int(self.perk_size/2)),self.radius,(255,255,255),thickness=-1)
        icon = cv2.bitwise_and(icon, icon, mask=circle_img)
        return icon
    
    def compare_perk(self):
        # self.process_screen_image()
        screen_perk = self.perk_file_processing(self.image[662:662+self.perk_size,303:303+self.perk_size])
        screen_perk = cv2.resize(screen_perk,(self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        cv2.imshow("Screen Perk",screen_perk)
        icon = cv2.imread(f"{os.getenv('PERK_LOCATION_SURVIVOR')}/Quick And Quiet.png")
        icon = self.perk_file_processing(icon)        
        icon = cv2.resize(icon, (self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        cv2.imshow("Perk Size",icon)
        
    def run(self):
        survivor_perks_used = []
        killer_perks_used = []
        
        survivor_perks_used = {}
        killer_perks_used = {}
        # Divides the screen into 20 spaces corresponding to each perk location.        
        # Player 1
        survivor_perks_used["player_1"] = {}
        survivor_perks_used["player_1"]["perk_1"] = self.find_best_matching_perk(self.image[310:310+self.perk_size,193:193+self.perk_size])
        survivor_perks_used["player_1"]["perk_2"] = self.find_best_matching_perk(self.image[310:310+self.perk_size,248:248+self.perk_size])
        survivor_perks_used["player_1"]["perk_3"] = self.find_best_matching_perk(self.image[310:310+self.perk_size,303:303+self.perk_size])
        survivor_perks_used["player_1"]["perk_4"] = self.find_best_matching_perk(self.image[310:310+self.perk_size,358:358+self.perk_size])

        # # Player 2
        survivor_perks_used["player_2"] = {}
        survivor_perks_used["player_2"]["perk_1"] = self.find_best_matching_perk(self.image[428:428+self.perk_size,193:193+self.perk_size])
        survivor_perks_used["player_2"]["perk_2"] = self.find_best_matching_perk(self.image[428:428+self.perk_size,248:248+self.perk_size])
        survivor_perks_used["player_2"]["perk_3"] = self.find_best_matching_perk(self.image[428:428+self.perk_size,303:303+self.perk_size])
        survivor_perks_used["player_2"]["perk_4"] = self.find_best_matching_perk(self.image[428:428+self.perk_size,358:358+self.perk_size])
        
        # # Player 3
        survivor_perks_used["player_3"] = {} 
        survivor_perks_used["player_3"]["perk_1"] = self.find_best_matching_perk(self.image[544:544+self.perk_size,193:193+self.perk_size])
        survivor_perks_used["player_3"]["perk_2"] = self.find_best_matching_perk(self.image[544:544+self.perk_size,248:248+self.perk_size])
        survivor_perks_used["player_3"]["perk_3"] = self.find_best_matching_perk(self.image[544:544+self.perk_size,303:303+self.perk_size])
        survivor_perks_used["player_3"]["perk_4"] = self.find_best_matching_perk(self.image[544:544+self.perk_size,358:358+self.perk_size])
        
        # # Player 4
        survivor_perks_used["player_4"] = {} 
        survivor_perks_used["player_4"]["perk_1"] = self.find_best_matching_perk(self.image[662:662+self.perk_size,193:193+self.perk_size])
        survivor_perks_used["player_4"]["perk_2"] = self.find_best_matching_perk(self.image[662:662+self.perk_size,248:248+self.perk_size])
        survivor_perks_used["player_4"]["perk_3"] = self.find_best_matching_perk(self.image[662:662+self.perk_size,303:303+self.perk_size])
        survivor_perks_used["player_4"]["perk_4"] = self.find_best_matching_perk(self.image[662:662+self.perk_size,358:358+self.perk_size])
                 
        # Killer Perks
        killer_perks_used["perk_1"] = self.find_best_matching_perk(self.image[771:771+self.perk_size,192:192+self.perk_size],False)
        killer_perks_used["perk_2"] = self.find_best_matching_perk(self.image[771:771+self.perk_size,246:246+self.perk_size],False)
        killer_perks_used["perk_3"] = self.find_best_matching_perk(self.image[771:771+self.perk_size,302:302+self.perk_size],False)
        killer_perks_used["perk_4"] = self.find_best_matching_perk(self.image[771:771+self.perk_size,356:356+self.perk_size],False)
        
        return survivor_perks_used, killer_perks_used