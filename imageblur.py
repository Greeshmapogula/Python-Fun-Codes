#### first step is open command prompt and run this command "pip install pillow" ####

#pil stands for Python Imaging Library
from PIL import Image, ImageFilter as IF

## here image module is used to open and display the image 
## Image filter has various functions to perform over images

#opening the image 
image = Image.open("python.jpg")##keep the image in same folder in which image is saved##

##applying the filter
img=image.filter(IF.BoxBlur(15))

#saving the image
img.save("saved.jpg")

#displaying blurred image
img.show() 