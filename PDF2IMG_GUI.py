import os
import tkinter as tk
from tkinter import filedialog
from pdf2image import convert_from_path
import subprocess
import time

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        pdf_to_images(file_path)

def pdf_to_images(pdf_path):
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

    convert_from_path(pdf_path, dpi=dpi, output_folder=output_folder, output_file=output_file, fmt=fmt)
    open_output_folder(output_folder)

def open_output_folder(folder_path):
    try:
        subprocess.Popen(["explorer", folder_path])
    except Exception as e:
        print("Failed to open folder:", e)

app = tk.Tk()
app.title("PDF to Image Converter")

select_button = tk.Button(app, text="Select PDF File", command=select_pdf_file)
select_button.pack(pady=20)

app.mainloop()
