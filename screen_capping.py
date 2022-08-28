import uuid
import pyautogui
import numpy as np
import cv2

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
        
    def calculate_brightness_vector(self,brightness):
        # If brightness is set to 1, then the variable bVector will 135
        fullBrightWhite = 135
        noBrightWhite = 100
        difference = fullBrightWhite - noBrightWhite
        bVector = noBrightWhite + (difference * float(brightness))
        return bVector
    
    def get_image_capture(self):
        fileName = f'{str(uuid.uuid4())}.png'
        image = pyautogui.screenshot()
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        # cv2.imwrite('processing/'+fileName, image)
        return image, fileName

    def get_image_from_filename(self, filename):
        fileName = f'filename.png'
        image = cv2.imread(filename)
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        return image, fileName
        