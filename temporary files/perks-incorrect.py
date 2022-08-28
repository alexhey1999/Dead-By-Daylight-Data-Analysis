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
    
    
    def get_perk_list(self):
        self.process_screen_image()
        return listdir(os.getenv("PERK_LOCATIONS"))
    
    
    def show_screen(self):
        # self.process_screen_image()
        cv2.imshow("Perk Screen ", self.image)
        
        
    def show_image(self, image,name="No Name Given"):
        cv2.imshow(name,image)
        
        
    def process_screen_image(self):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([145, 145, 145])
        mask = cv2.inRange(self.image, lower_white, upper_white)
        WhiteBackground = np.zeros((self.image.shape[0], self.image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((self.image.shape[0], self.image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        self.image = result
        
    def process_perk_image(self,perk):
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([145, 145, 145])
        mask = cv2.inRange(perk, lower_white, upper_white)
        WhiteBackground = np.zeros((perk.shape[0], perk.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((perk.shape[0], perk.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        return result
    
    def process_perk_screen_image(self,perk_screen_image):
        height,width,_ = perk_screen_image.shape
        mask = np.zeros((height,width), np.uint8)
        circle_img = cv2.circle(mask,(25,25),15,(255,255,255),thickness=-1)        
        perk_screen_image = cv2.bitwise_and(perk_screen_image, perk_screen_image, mask=circle_img)
        perk_screen_image = cv2.resize(perk_screen_image, (self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        return(perk_screen_image)
    
    def find_best_matching_perk(self,image_to_analyze):
            most_probable_perk = None
            most_probable_perk_score = 0
            second_probable_perk = None
            second_probable_perk_score = 0
            for perk in self.get_perk_list():
                icon = cv2.imread(f"{os.getenv('PERK_LOCATIONS')}/{perk}")
                icon = self.process_perk_image(icon)
                icon = cv2.resize(icon, (self.perk_size, self.perk_size),interpolation=cv2.INTER_AREA)
                result = cv2.matchTemplate(image_to_analyze, icon, cv2.TM_CCOEFF_NORMED)
                minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)
                if maxVal > most_probable_perk_score:
                    second_probable_perk_score = most_probable_perk_score
                    most_probable_perk_score = maxVal
                    second_probable_perk = most_probable_perk
                    most_probable_perk = perk

            return most_probable_perk, most_probable_perk_score,second_probable_perk,second_probable_perk_score
            
    
    def perk_checker_and_display(self,screen,name="Perk",show_image = False,show_second_best = False):
        if show_image: self.show_image(screen,name)
        perk_chosen, perk_score,perk_2_chosen, perk_2_score = self.find_best_matching_perk(screen)
        print("Perk Chosen: ", perk_chosen)
        if show_second_best:
            print("Perk Score: ", perk_score)
            print("Perk 2 Chosen: ", perk_2_chosen)
            print("Perk 2 Score: ", perk_2_score)    
    
    def size_comparison(self):
        self.process_screen_image()

        screen_perk = self.image[542:542+self.perk_size,193:193+self.perk_size]
        height,width,_ = screen_perk.shape
        mask = np.zeros((height,width), np.uint8)
        circle_img = cv2.circle(mask,(25,25),15,(255,255,255),thickness=-1)        
        screen_perk = cv2.bitwise_and(screen_perk, screen_perk, mask=circle_img)
        screen_perk = cv2.resize(screen_perk, (self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
  
  
        self.show_image(screen_perk,"Screen Perks")

        icon = cv2.imread(f"{os.getenv('PERK_LOCATIONS')}/iconPerks_vigil.png")
        icon = self.process_perk_image(icon)
        icon = cv2.resize(icon, (self.perk_size, self.perk_size),interpolation=cv2.INTER_AREA)
        icon = cv2.resize(icon, (self.perk_size * 10, self.perk_size * 10),interpolation=cv2.INTER_AREA)
        self.show_image(icon,"Perk Size")
    
        
    
    def divide_screen(self):
        # Divides the screen into 20 spaces corresponding to each perk location.
        self.process_screen_image()
        # Width Then Height
        # Player 1
        player_1_perk_1 = self.process_perk_screen_image(self.image[310:310+self.perk_size,193:193+self.perk_size])
        self.perk_checker_and_display(player_1_perk_1)
        
        player_1_perk_2 = self.process_perk_screen_image(self.image[310:310+self.perk_size,248:248+self.perk_size])
        self.perk_checker_and_display(player_1_perk_2)
        
        player_1_perk_3 = self.process_perk_screen_image(self.image[310:310+self.perk_size,303:303+self.perk_size])
        self.perk_checker_and_display(player_1_perk_3)
        
        player_1_perk_4 = self.process_perk_screen_image(self.image[310:310+self.perk_size,358:358+self.perk_size])
        self.perk_checker_and_display(player_1_perk_4)
        
        # Player 2
        player_2_perk_1 = self.process_perk_screen_image(self.image[426:426+self.perk_size,193:193+self.perk_size])
        self.perk_checker_and_display(player_2_perk_1,"Perk 1")
        
        player_2_perk_2 = self.process_perk_screen_image(self.image[426:426+self.perk_size,248:248+self.perk_size])
        self.perk_checker_and_display(player_2_perk_2, "Perk 2")
        
        player_2_perk_3 = self.process_perk_screen_image(self.image[426:426+self.perk_size,303:303+self.perk_size])
        self.perk_checker_and_display(player_2_perk_3, "Perk 3")
        
        player_2_perk_4 = self.process_perk_screen_image(self.image[426:426+self.perk_size,358:358+self.perk_size])
        self.perk_checker_and_display(player_2_perk_4, "Perk 4")
        
        
        
        # Player 2
        player_3_perk_1 = self.process_perk_screen_image(self.image[542:542+self.perk_size,193:193+self.perk_size])
        self.perk_checker_and_display(player_3_perk_1,"Perk 1",True)
        
        player_3_perk_2 = self.process_perk_screen_image(self.image[542:542+self.perk_size,248:248+self.perk_size])
        self.perk_checker_and_display(player_3_perk_2, "Perk 2",True)
        
        player_3_perk_3 = self.process_perk_screen_image(self.image[542:542+self.perk_size,303:303+self.perk_size])
        self.perk_checker_and_display(player_3_perk_3, "Perk 3",True)
        
        player_3_perk_4 = self.process_perk_screen_image(self.image[542:542+self.perk_size,358:358+self.perk_size])
        self.perk_checker_and_display(player_3_perk_4, "Perk 4",True)
        
        
        # Player 4
        player_4_perk_1 = None
        player_4_perk_2 = None
        player_4_perk_3 = None
        player_4_perk_4 = None
                 
        # Killer Perks
        killer_perk_1 = None
        killer_perk_2 = None
        killer_perk_3 = None
        killer_perk_4 = None
        pass