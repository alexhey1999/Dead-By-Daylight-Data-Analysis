import uuid
import pyautogui
import numpy as np
import PIL.Image as Image
import cv2

class Screen():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.lower_white = 105
        self.brightness_scalar = 3.7
        
    def calculate_and_set_brightness_vector(self,image):
        image = Image.fromarray(image)
        greyscale_image = image.convert('L')
        histogram = greyscale_image.histogram()
        pixels = sum(histogram)
        brightness = scale = len(histogram)

        for index in range(0, scale):
            ratio = histogram[index] / pixels
            brightness += ratio * (-scale + index)

        brightness_value = 1 if brightness == 255 else brightness / scale
        lower_white_calculation = (brightness_value * self.brightness_scalar) * self.lower_white
        self.lower_white = round(lower_white_calculation)
        return(self.lower_white)
    
    def get_image_capture(self):
        fileName = f'{str(uuid.uuid4())}.png'
        image = pyautogui.screenshot()
        # image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        # cv2.imwrite('processing/'+fileName, image)
        return image, fileName

    def get_image_from_filename(self, filename):
        fileName = f'filename.png'
        image = cv2.imread(filename)
        # image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        image = cv2.resize(image, (1920, 1080))
        return image, fileName
    
    def process_screen_image(self,image):
        self.calculate_and_set_brightness_vector(image)
        upper_white = np.array([256, 256, 256])
        lower_white = np.array([self.lower_white, self.lower_white, self.lower_white])
        mask = cv2.inRange(image, lower_white, upper_white)
        WhiteBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        WhiteBackground[:,:,:] = (255,255,255)
        BlackBackground = np.zeros((image.shape[0], image.shape[1], 3), dtype=np.uint8)
        BlackBackground[:,:,:] = (0,0,0)
        result = cv2.bitwise_and(WhiteBackground,WhiteBackground,BlackBackground ,mask = mask)
        return result
    
    def show_image(self, image,name="No Name Given"):
        cv2.imshow(name,image)