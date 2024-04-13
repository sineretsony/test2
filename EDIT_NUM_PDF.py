from PyPDF2 import PdfReader, PdfWriter

# Path to the input PDF file
input_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file.pdf"

# Path to save the modified PDF file
output_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file_with_pixel.pdf"

# Open the existing PDF file
with open(input_pdf_path, "rb") as file:
    pdf_reader = PdfReader(file)
    pdf_writer = PdfWriter()

    # Get the first page
    page = pdf_reader.pages[0]

    # Create a new page with a 1x1 white pixel in the top left corner
    page.mediabox.upper_right = (1, 1)

    # Add the modified page to the PDF file
    pdf_writer.add_page(page)

    # Save the changes to a new PDF file
    with open(output_pdf_path, "wb") as output_file:
        pdf_writer.write(output_file)

print("Added a 1x1 white pixel in the top left corner of the first page of the PDF file.")
