import fitz  # PyMuPDF

# Путь к исходному PDF-файлу
input_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file.pdf"

# Открываем PDF-файл
pdf_document = fitz.open(input_pdf_path)

# Получаем первую страницу
page = pdf_document[0]

# Добавляем текст "2347" красным цветом в левый верхний угол
text = "2347"
font_size = 24
font_color = (1, 0, 0)  # Красный цвет
page.insert_text((10, 10), text, fontsize=font_size, color=font_color)

# Сохраняем изменения
output_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file_with_text.pdf"
pdf_document.save(output_pdf_path)

# Закрываем PDF-файл
pdf_document.close()

print("Добавлен текст '2347' красным цветом в левый верхний угол первой страницы PDF-файла.")
