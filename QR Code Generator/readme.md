========================================
        QR CODE GENERATOR PROJECT
========================================

Project Title:
QR Code Generator using Python

----------------------------------------
Project Description:
----------------------------------------
This project is a simple QR Code Generator 
developed using Python. It allows users to 
enter any text or URL and generates a QR code 
image file automatically.

The generated QR code is saved as a PNG file 
in the project folder.

----------------------------------------
Features:
----------------------------------------
- Generate QR code for any text
- Generate QR code for any URL
- Saves output as PNG image
- Customizable size and border
- Simple and beginner-friendly program

----------------------------------------
Technologies Used:
----------------------------------------
- Python 3.10 or above
- qrcode library
- Pillow (PIL)

----------------------------------------
Installation Steps:
----------------------------------------
1. Install Python (3.10 or above).
2. Open Command Prompt.
3. Install required library using:

   python -m pip install qrcode[pil]

----------------------------------------
How to Run the Program:
----------------------------------------
1. Open terminal in project folder.
2. Run the command:

   python qr_generator.py

3. Enter text or URL when prompted.
4. The QR code will be saved as:

   my_qrcode.png

----------------------------------------
Sample Code:
----------------------------------------
import qrcode

data = input("Enter text or URL: ")

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=5
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("my_qrcode.png")

print("QR Code generated successfully!")

----------------------------------------
Future Enhancements:
----------------------------------------
- Add GUI interface
- Add logo inside QR code
- Create bulk QR generator
- Convert into web application

----------------------------------------
Author:
----------------------------------------
Sonali Priyadharshini
Python Developer
========================================