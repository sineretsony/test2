from PyPDF2 import PdfReader, PdfWriter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

# Path to your existing PDF file
existing_pdf = r"C:\Users\gorea\Desktop\Новая папка\Untitled-1.pdf"
# Path to the new PDF file with the added text
new_pdf = r"C:\Users\gorea\Desktop\Новая папка\Untitled-1_with_text.pdf"

# Open the existing PDF file for reading
input_pdf = PdfReader(existing_pdf)

# Create a PdfWriter object to write the modified PDF
output_pdf = PdfWriter()

# Copy the contents of the existing PDF to the PdfWriter object
for page in input_pdf.pages:
    output_pdf.add_page(page)

# Create a canvas object to work with the PDF
c = canvas.Canvas("temp.pdf")

# Register the Arial font
pdfmetrics.registerFont(TTFont('Arial', 'C:/Windows/Fonts/arial.ttf'))

# Set the font and text size
c.setFont("Arial", 8)

# Text position (top left corner)
x = 10
y = 800

# Add text to the temporary PDF
c.drawString(x, y, "119567")

# Save the canvas
c.save()

# Open the temporary PDF file for reading and add its contents to output_pdf
temp_pdf = PdfReader("temp.pdf")
for page in temp_pdf.pages:
    output_pdf.add_page(page)

# Save the combined PDF to a new file
with open(new_pdf, "wb") as output_stream:
    output_pdf.write(output_stream)

# Remove the temporary PDF file
import os
os.remove("temp.pdf")
