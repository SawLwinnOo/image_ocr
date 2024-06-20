import cv2
import pytesseract
import time
import tkinter as tk
from tkinter import filedialog

def browse_image():
    # Create a Tkinter root window (it will not be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(
        title="Select an Image",
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.tiff")]
    )

    return file_path

# Get the image file path from the user
image_path = browse_image()

# Check if a file path was selected
if image_path:
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Convert image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Perform OCR using pytesseract
    custom_config = r'--oem 3 --psm 6'  # OCR Engine Mode (OEM) and Page Segmentation Mode (PSM) settings
    text = pytesseract.image_to_string(gray_image, config=custom_config)

    # Split the recognized text into lines and add to a list
    text_lines = text.splitlines()

    # Print recognized text line by line every five seconds
    print("Recognized Text:")
    for line in text_lines:
        print(line)
        time.sleep(5)  # Wait for 5 seconds before printing the next line

    # You can also print the list to see the text lines
    print("Text lines as list:")
    print(text_lines)
else:
    print("No file selected.")