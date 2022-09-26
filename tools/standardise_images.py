from os import listdir
import PIL.Image as Image


def imageFix(location):

    imageList = listdir(location)

    for fileName in imageList:

        image = Image.open(location+fileName)
        image = image.convert("RGBA")
        canvas = Image.new('RGBA', image.size, (0,0,0,255)) # Empty canvas colour (r,g,b,a)
        canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
        canvas.save(str(location+fileName), format="PNG")   
        
if __name__ == "__main__":
    imageFix('./Images/Help/')