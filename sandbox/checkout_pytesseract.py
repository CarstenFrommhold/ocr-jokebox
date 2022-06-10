"""
Checkout Tesseract

https://github.com/madmaze/pytesseract
Install tesseract first (https://github.com/tesseract-ocr/tesseract)

Support for OpenCV which might help to preprocess
"""
import pytesseract
from PIL import Image


img = Image.open("../pictures/to_be_ocr.png")
# img = Image.open("../pictures/20220609_195936.jpg")
img = Image.open("../pic/pic.jpg")
print(pytesseract.image_to_string(img))

# import pytesseract
# import cv2
#
# img = cv2.imread("../pictures/20220609_195936.jpg")
# print(pytesseract.image_to_string(img))
