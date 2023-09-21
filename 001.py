import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.rl_config import canvas_basefontName

def extract_number_from_filename(filename):
    # Извлекаем первое число из имени файла
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    return 0

def duplicate_pages_with_number(filename, num_duplicates):
    # Получаем содержимое исходного PDF
    content = []
    original_basefont = canvas_basefontName
    canvas_basefontName = "Helvetica"
    c = canvas.Canvas("temp.pdf", pagesize=letter)
    for page_num in range(num_duplicates):
        c.setFont(original_basefont, 12)
        c.showPage()
        content.append(c.pages[page_num])
    c.save()
    canvas_basefontName = original_basefont

    # Создаем новый PDF-файл и копируем содержимое исходных страниц
    new_filename = os.path.splitext(filename)[0] + f"_duplicated.pdf"
    c = canvas.Canvas(new_filename, pagesize=letter)
    for page in content:
        c.setPageSize((page.width, page.height))
        c.doForm(c.getPageNumber(), page)
        c.showPage()
    c.save()

    # Удаляем временный файл
    os.remove("temp.pdf")

def main(path):
    for filename in os.listdir(path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(path, filename)
            num_duplicates = extract_number_from_filename(filename)
            if num_duplicates > 0:
                duplicate_pages_with_number(full_path, num_duplicates)

if __name__ == "__main__":
    directory_path = r"C:\Users\gorea\Desktop\00"
    main(directory_path)
