# Requirements: qrcode reportlab

import os
import qrcode
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Get input to generate the QR code
input_data = input("Enter the data to be stored in the QR code: ")
filename = input("Enter the filename for the PDF: ")

# Generate a QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
qr.add_data(input_data)
qr.make(fit=True)

# Create an image of the QR code
img = qr.make_image(fill_color="black", back_color="white")
qr_image_path = 'qrcode.png'
img.save(qr_image_path)

# Create a PDF with the barcode
pdf_file_path = filename
c = canvas.Canvas(pdf_file_path, pagesize=letter)
c.drawImage('qrcode.png', x=0, y=000, width=185, height=185)
c.save()

print(f"PDF generated with barcode at {pdf_file_path}")

# Clean up the QR code image
os.remove(qr_image_path)
