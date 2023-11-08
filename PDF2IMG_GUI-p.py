import os
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
import subprocess
import time
from PIL import Image, ImageEnhance
import pyocr
import codecs

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_to_images_and_ocr(file_path)

def pdf_to_images_and_ocr(pdf_path):
    dpi = 300

    # Get the user's desktop directory
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    # Ensure the output folder exists, create it if not
    output_folder = os.path.join(desktop_path, "PDFConversionOutput")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    timestamp = time.strftime("%Y%m%d%H%M%S")
    output_file = f'{base_name}_{timestamp}'
    fmt = 'png'

    images = convert_from_path(pdf_path, dpi=dpi, output_folder=output_folder, output_file=output_file, fmt=fmt)

    for image in images:
        enhance_and_ocr(image)

def enhance_and_ocr(img):
    # Enhancing Image
    img_g = img.convert('L')  # Gray Conversion
    enhancer = ImageEnhance.Contrast(img_g)  # Increasing Contrast
    img_con = enhancer.enhance(2.0)  # Increasing Contrast

    # "Reading" the text and extracting it
    builder = pyocr.builders.TextBuilder(tesseract_layout=6)
    text = tool.image_to_string(img_con, lang="jpn", builder=builder)

    # Writing text to txt
    print(text, file=codecs.open('output.txt', 'a', 'utf-8'))

def open_output_folder(folder_path):
    try:
        subprocess.Popen(["explorer", folder_path])
    except Exception as e:
        print("Failed to open folder:", e)

app = tk.Tk()
app.title("PDF to Image Converter and OCR")

select_button = tk.Button(app, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=20)

# Path Setting for Tesseract
path = 'C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path
pyocr.tesseract.TESSERACT_CMD = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
tools = pyocr.get_available_tools()
tool = tools[0]

app.mainloop()