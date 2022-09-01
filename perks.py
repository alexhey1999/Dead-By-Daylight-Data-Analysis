import os
from os import listdir
import cv2
import numpy as np

class Perks:
    def __init__(self, image, brightness_vector):
        self.image = image
        self.brightness_vector = brightness_vector
        self.perk_size = 50
        self.perk_image_size = 40
    
    
    def set_image(self, image):
        self.image = image
    
    
    def get_perk_list(self,perk_path):
        return listdir(perk_path)
    
    
    def show_screen(self):
        # self.process_screen_image()
        cv2.imshow("Perk Screen ", self.image)
    
        
    def show_image(self, image,name="No Name Given"):
        cv2.imshow(name,image)
    
        
    def process_screen_image(self):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([105, 105, 105])
        mask = cv2.inRange(self.image, lower_white, upper_white)
        WhiteBackground = np.zeros((self.image.shape[0], self.image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((self.image.shape[0], self.image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        self.image = result
    
        
    def process_perk_image(self,perk):
        cv2.imshow(perk,'Testing')    
        return perk
    
    
    def process_perk_screen_image(self,perk_screen_image):
        height,width,_ = perk_screen_image.shape
        mask = np.zeros((height,width), np.uint8)
        circle_img = cv2.circle(mask,(25,25),16,(255,255,255),thickness=-1)        
        perk_screen_image = cv2.bitwise_and(perk_screen_image, perk_screen_image, mask=circle_img)
        return(perk_screen_image)
    
    
    def find_best_matching_perk(self,image_to_analyze, survivor = True):
            if survivor:
                perk_path = os.getenv('PERK_LOCATIONS_SURVIVOR')
            else:
                perk_path = os.getenv('PERK_LOCATIONS_KILLER')
            most_probable_perk = None
            most_probable_perk_score = 0
            for perk in self.get_perk_list(perk_path):
                icon = cv2.imread(f"{perk_path}/{perk}")
                icon = cv2.resize(icon, (self.perk_size, self.perk_size),interpolation=cv2.INTER_AREA)
                # icon = self.process_perk_image(icon)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_perk_score:
                    most_probable_perk_score = maxVal
                    most_probable_perk = perk
                    
                if most_probable_perk:
                    most_probable_perk
            return most_probable_perk.split('.')[0]
            
    
    def perk_checker_and_display(self,screen,name="Perk",survivor = True, show_image = False):
        if show_image: self.show_image(screen,name)
        perk_chosen, perk_score = self.find_best_matching_perk(screen,survivor)
        print("Perk Chosen: ", perk_chosen)
    
    
    def size_comparison(self):
        self.process_screen_image()
        screen_perk = self.process_perk_screen_image(self.image[770:770+self.perk_size,303:303+self.perk_size])
        screen_perk = cv2.resize(screen_perk,(self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        self.show_image(screen_perk,"Screen Perk")
        icon = cv2.imread(f"{os.getenv('PERK_LOCATIONS_KILLER')}/iconPerks_enduring.png")
        icon = cv2.resize(icon, (self.perk_size, self.perk_size),interpolation=cv2.INTER_AREA)
        icon = cv2.resize(icon, (self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        self.show_image(icon,"Perk Size")
        
        
    def run(self):
        survivor_perks_used = []
        killer_perks_used = []
        
        # Divides the screen into 20 spaces corresponding to each perk location.
        self.process_screen_image()
        
        # Player 1
        player_1_perk_1 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[310:310+self.perk_size,193:193+self.perk_size])))     
        player_1_perk_2 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[310:310+self.perk_size,248:248+self.perk_size])))    
        player_1_perk_3 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[310:310+self.perk_size,303:303+self.perk_size])))
        player_1_perk_4 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[310:310+self.perk_size,358:358+self.perk_size])))
 
        # # Player 2
        player_2_perk_1 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[426:426+self.perk_size,193:193+self.perk_size])))
        player_2_perk_2 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[426:426+self.perk_size,248:248+self.perk_size])))
        player_2_perk_3 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[426:426+self.perk_size,303:303+self.perk_size])))
        player_2_perk_4 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[426:426+self.perk_size,358:358+self.perk_size])))
        
        # # Player 3
        player_3_perk_1 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[544:544+self.perk_size,193:193+self.perk_size]))) 
        player_3_perk_2 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[544:544+self.perk_size,248:248+self.perk_size])))
        player_3_perk_3 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[544:544+self.perk_size,303:303+self.perk_size])))
        player_3_perk_4 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[544:544+self.perk_size,358:358+self.perk_size])))
        
        # # Player 4
        player_4_perk_1 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[662:662+self.perk_size,193:193+self.perk_size])))
        player_4_perk_2 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[662:662+self.perk_size,248:248+self.perk_size])))
        player_4_perk_3 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[662:662+self.perk_size,303:303+self.perk_size])))
        player_4_perk_4 = survivor_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[662:662+self.perk_size,358:358+self.perk_size])))
                 
        # Killer Perks
        killer_perk_1 = killer_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[770:770+self.perk_size,193:193+self.perk_size]),False)) 
        killer_perk_2 = killer_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[770:770+self.perk_size,248:248+self.perk_size]),False))
        killer_perk_3 = killer_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[770:770+self.perk_size,303:303+self.perk_size]),False))
        killer_perk_4 = killer_perks_used.append(self.find_best_matching_perk(self.process_perk_screen_image(self.image[770:770+self.perk_size,358:358+self.perk_size]),False))
        
        return survivor_perks_used, killer_perks_used