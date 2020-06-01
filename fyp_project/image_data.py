import pytesseract
from PIL import Image
img=Image.open('static/images/main-img.png')
text=pytesseract.image_to_string(img)
print(text)