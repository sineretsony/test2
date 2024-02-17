import PyPDF2

# Путь к исходному PDF-файлу
input_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file.pdf"

# Открываем PDF-файл для чтения
with open(input_pdf_path, "rb") as input_pdf_file:
    pdf_reader = PyPDF2.PdfReader(input_pdf_file)

    # Создаем объект для записи измененного PDF-файла
    output_pdf = PyPDF2.PdfWriter()

    # Копируем содержимое исходного файла в новый файл
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        # Делаем небольшое смещение
        upper_right_x, upper_right_y = page.mediabox.upper_right
        page.mediabox.upper_right = (upper_right_x - 1, upper_right_y)
        output_pdf.add_page(page)

    # Путь для сохранения измененного файла
    output_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file_with_offset.pdf"

    # Открываем файл для записи
    with open(output_pdf_path, "wb") as output_pdf_file:
        output_pdf.write(output_pdf_file)

print("Выполнено небольшое смещение первой страницы в PDF-файле.")
