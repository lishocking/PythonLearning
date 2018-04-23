import pytesseract
from PIL import Image
img=Image.open("./1.bmp")
pytesseract.image_to_string(img)
