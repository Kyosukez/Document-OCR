# Importing Libraries 
import os
from PIL import Image, ImageEnhance
from pdf2image import convert_from_path
import pyocr
import codecs

# Path Setting
path='Set Path To File'
os.environ['PATH'] = os.environ['PATH'] + path

# Retrieving the OCR engine 
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

# loading image
img = Image.open('sample.png')

# Enhancing Image
img_g = img.convert('L') # Gray Conversion 
enhancer= ImageEnhance.Contrast(img_g) # Increasing Contrast
img_con = enhancer.enhance(2.0) #Increasing Contrast 

# "Reading" the text and extracting it 
builder = pyocr.builders.TextBuilder(tesseract_layout=6)
text = tool.image_to_string(img, lang="jpn", builder=builder)

# Writing text to txt
print(text, file=codecs.open('output.txt', 'w', 'utf-8'))