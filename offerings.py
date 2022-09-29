import os
from os import listdir
from subprocess import CREATE_NEW_PROCESS_GROUP
import cv2
import numpy as np

class Offerings:
    def __init__(self, image):
        self.image = image        
        
        self.offering_size = 47
        self.file_offering_margin = 1
        self.compress_image = 40
        self.radius = 21

    
    def set_image(self, image):
        self.image = image
    
    
    def get_offering_list(self,perk_path):
        return listdir(perk_path)
    
    
    def file_offering_processing(self,image):
        img_file = cv2.resize(image,(int(self.compress_image),int(self.compress_image)))
        img_file = cv2.resize(img_file,(int(self.offering_size),int(self.offering_size)))
        img_file = img_file[self.file_offering_margin:-self.file_offering_margin, self.file_offering_margin:-self.file_offering_margin]
        return img_file
    
    def screen_offering_processing(self,image):
        mask = np.zeros((self.offering_size, self.offering_size), np.uint8)
        circle_img = cv2.circle(mask,(int(self.offering_size/2),int(self.offering_size/2)),self.radius,(255,255,255),thickness=-1)
        image = cv2.bitwise_and(image, image, mask=circle_img)
        return image
    
    def find_best_matching_offering(self,image_to_analyze):
            image_to_analyze = self.screen_offering_processing(image_to_analyze)
            offering_path = os.getenv('OFFERING_LOCATION')
            most_probable_offering = None
            most_probable_offering_score = 0
            for offering in self.get_offering_list(offering_path):
                icon = cv2.imread(f"{offering_path}/{offering}",1)
                icon =  self.file_offering_processing(icon)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_offering_score:
                    most_probable_offering_score = maxVal
                    most_probable_offering = offering
                    
            if most_probable_offering:
                return most_probable_offering.split('.')[0]
            else:
                return "No Offering"
    
    
    def compare_offering(self):
        screen_img = self.image[773:773+self.offering_size,422:422+self.offering_size]
        screen_img = self.screen_offering_processing(screen_img)
        screen_img = cv2.resize(screen_img,(self.offering_size*5,self.offering_size*5))
        cv2.imshow("Screen Image",screen_img)
        
        img_file = cv2.imread(os.getenv('OFFERING_LOCATION')+'/Escape Cake.png')
        img_file = self.file_offering_processing(img_file)
        img_file = cv2.resize(img_file,(self.offering_size*5,self.offering_size*5))
        cv2.imshow("File Image",img_file)
    
    def run(self):
        offerings_used = []
        
        
        # Divides the screen into 5 spaces corresponding to each perk location.        
        # Player 1
        offerings_used.append(self.find_best_matching_offering(self.image[313:313+self.offering_size,424:424+self.offering_size]))

        # # Player 2
        offerings_used.append(self.find_best_matching_offering(self.image[431:431+self.offering_size,424:424+self.offering_size]))
        
        # # Player 3
        offerings_used.append(self.find_best_matching_offering(self.image[547:547+self.offering_size,424:424+self.offering_size]))
        
        # # Player 4
        offerings_used.append(self.find_best_matching_offering(self.image[666:666+self.offering_size,424:424+self.offering_size]))
                 
        # Killer Offering Used
        offerings_used.append(self.find_best_matching_offering(self.image[773:773+self.offering_size,422:422+self.offering_size]))
        
        offerings_used= list(filter(lambda offering:offering != "No Offering",offerings_used))
        
        return offerings_used