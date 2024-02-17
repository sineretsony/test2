import fitz  # PyMuPDF

# Путь к исходному PDF-файлу
input_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file.pdf"

# Открываем PDF-файл
pdf_document = fitz.open(input_pdf_path)

# Получаем первую страницу
page = pdf_document[0]

# Добавляем прямоугольник 1x1 пиксель белого цвета в левом верхнем углу
rect = fitz.Rect(0, page.rect.height, 1, page.rect.height - 1)  # x0, y0, x1, y1
page.draw_rect(rect, fill=(1, 1, 1))  # fill=(R, G, B)

# Сохраняем изменения
output_pdf_path = r"C:\Users\gorea\Desktop\Новая папка\file_with_pixel.pdf"
pdf_document.save(output_pdf_path)

# Закрываем PDF-файл
pdf_document.close()

print("Добавлена точка 1x1 пиксель белого цвета в левый верхний угол первой страницы PDF-файла.")
