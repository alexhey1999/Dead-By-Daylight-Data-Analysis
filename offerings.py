import os
from os import listdir
import cv2
import numpy as np

class Offerings:
    def __init__(self, image):
        self.image = image
        self.offering_size = 48
        self.radius = 18

    
    def set_image(self, image):
        self.image = image
    
    
    def get_offering_list(self,perk_path):
        return listdir(perk_path)
    
    
    def find_best_matching_offering(self,image_to_analyze):
            offering_path = os.getenv('OFFERING_LOCATION')
            most_probable_offering = None
            most_probable_offering_score = 0
            for offering in self.get_offering_list(offering_path):
                icon = cv2.imread(f"{offering_path}/{offering}",1)
                icon = self.offering_file_processing(icon)
                
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                # result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_SQDIFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_offering_score:
                    most_probable_offering_score = maxVal
                    most_probable_offering = offering
                    
            if most_probable_offering:
                return most_probable_offering.split('.')[0]
            else:
                return "No Offering"
    
    def offering_file_processing(self,icon):
        # cv2.cvtColor(icon, cv2.COLOR_HSV2BGR)
        icon = cv2.resize(icon, (self.offering_size, self.offering_size),interpolation=cv2.INTER_AREA)
        mask = np.zeros((self.offering_size, self.offering_size), np.uint8)
        circle_img = cv2.circle(mask,(25,25),self.radius,(255,255,255),thickness=-1)
        icon = cv2.bitwise_and(icon, icon, mask=circle_img)
        return icon
    
    def compare_offering(self):
        screen_img = self.image[428:428+self.offering_size,423:423+self.offering_size]
        screen_img = cv2.resize(screen_img,(self.offering_size*5,self.offering_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('OFFERING_LOCATION')+'/Bound Envelope.png')
        img_file = cv2.resize(img_file,(self.offering_size*5,self.offering_size*5))
        cv2.imshow("File Image",img_file)
        
    def run(self):
        offerings_used = []
        
        
        # Divides the screen into 20 spaces corresponding to each perk location.        
        # Player 1
        offerings_used.append(self.find_best_matching_offering(self.image[312:312+self.offering_size,423:423+self.offering_size]))

        # # Player 2
        offerings_used.append(self.find_best_matching_offering(self.image[428:428+self.offering_size,423:423+self.offering_size]))
        
        # # Player 3
        offerings_used.append(self.find_best_matching_offering(self.image[546:546+self.offering_size,423:423+self.offering_size]))
        
        # # Player 4
        offerings_used.append(self.find_best_matching_offering(self.image[664:664+self.offering_size,423:423+self.offering_size]))
                 
        # Killer Offering Used
        offerings_used.append(self.find_best_matching_offering(self.image[773:773+self.offering_size,423:423+self.offering_size]))
        
        offerings_used= list(filter(lambda offering:offering != "No Offering",offerings_used))
        
        return offerings_used