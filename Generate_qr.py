# import random
# import string
# import qrcode
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
# import os
# import openpyxl
#
#
# # Генерация случайного кода
# def generate_code(length=40):
#     return ''.join(
#         random.choices(string.ascii_uppercase + string.digits, k=length))
#
#
# # Создание QR кода и сохранение его как векторного PDF
# def save_qr_code_as_pdf(code, url, output_folder):
#     qr_img = qrcode.make(url)
#     pdf_path = os.path.join(output_folder, f"{code}.pdf")
#
#     # Создаем PDF с помощью reportlab
#     c = canvas.Canvas(pdf_path, pagesize=letter)
#     qr_img.save("temp.png")  # Временный файл для сохранения QR кода
#
#     # Вставляем картинку на PDF
#     c.drawImage("temp.png", 100, 600, 200, 200)  # Позиция и размер QR кода
#     c.save()
#
#     os.remove("temp.png")  # Удаляем временный файл
#
#
# # Основная функция для генерации QR кодов и их статусов
# def generate_qr_codes(num_codes, output_folder):
#     codes_dict = {}
#
#     # Генерируем уникальные коды
#     while len(codes_dict) < num_codes:
#         code = generate_code()
#         if code not in codes_dict:
#             codes_dict[code] = 'new'
#
#     # Создаем QR коды и меняем статус на ok
#     for code in codes_dict:
#         url = f"https://play.google.com/store/games?code={code}"
#         save_qr_code_as_pdf(code, url, output_folder)
#         codes_dict[code] = 'ok'
#
#     return codes_dict
#
#
# # Создание Excel файла с кодами и их статусами
# def create_excel(codes_dict, output_folder):
#     wb = openpyxl.Workbook()
#     ws = wb.active
#     ws.append(['Code', 'Status'])
#
#     for code, status in codes_dict.items():
#         ws.append([code, status])
#
#     excel_path = os.path.join(output_folder, "qr_codes_status.xlsx")
#     wb.save(excel_path)
#
#
# # Основной процесс
# def main():
#     num_codes = 10  # Количество QR кодов
#     output_folder = "qr_codes"  # Папка для сохранения
#
#     # Создаем папку если ее нет
#     if not os.path.exists(output_folder):
#         os.makedirs(output_folder)
#
#     # Генерация QR кодов и их статусов
#     codes_dict = generate_qr_codes(num_codes, output_folder)
#
#     # Создание Excel файла
#     create_excel(codes_dict, output_folder)
#     print(
#         f"Генерация завершена. QR коды и таблица сохранены в папке {output_folder}")
#
#
# if __name__ == "__main__":
#     main()


import random
import string
import qrcode
import os
import openpyxl
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import svgwrite


# Генерация случайного кода
def generate_code(length=40):
    return ''.join(
        random.choices(string.ascii_uppercase + string.digits, k=length))


# Создание QR-кода и сохранение его как векторного PDF
def save_qr_code_as_pdf(code, url, output_folder):
    # Генерация QR-кода
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Сохраняем QR-код как SVG с использованием svgwrite
    svg_output = BytesIO()
    dwg = svgwrite.Drawing(size=(qr.modules_count * 10, qr.modules_count * 10))
    for row_index, row in enumerate(qr.modules):
        for col_index, module in enumerate(row):
            if module:
                dwg.add(dwg.rect(
                    insert=(col_index * 10, row_index * 10),
                    size=(10, 10),
                    fill='black'
                ))
    svg_data = dwg.tostring()

    # Преобразуем SVG в векторное изображение для PDF
    drawing = svg2rlg(BytesIO(svg_data.encode()))

    # Создаем PDF
    pdf_path = os.path.join(output_folder, f"{code}.pdf")
    c = canvas.Canvas(pdf_path)

    # Размер PDF совпадает с размером QR-кода
    c.setPageSize((drawing.width, drawing.height))

    # Вставляем векторное изображение QR-кода в PDF
    renderPDF.draw(drawing, c, 0, 0)
    c.save()


# Основная функция для генерации QR-кодов и их статусов
def generate_qr_codes(num_codes, output_folder):
    codes_dict = {}

    # Генерируем уникальные коды
    while len(codes_dict) < num_codes:
        code = generate_code()
        if code not in codes_dict:
            codes_dict[code] = 'new'

    # Создаем QR-коды и меняем статус на ok
    for code in codes_dict:
        url = f"https://play.google.com/store/games?code={code}"
        save_qr_code_as_pdf(code, url, output_folder)
        codes_dict[code] = 'ok'

    return codes_dict


# Создание Excel файла с кодами и их статусами
def create_excel(codes_dict, output_folder):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.append(['Code', 'Status'])

    for code, status in codes_dict.items():
        ws.append([code, status])

    excel_path = os.path.join(output_folder, "qr_codes_status.xlsx")
    wb.save(excel_path)


# Основной процесс
def main():
    num_codes = 10  # Количество QR кодов
    output_folder = "qr_codes"  # Папка для сохранения

    # Создаем папку если ее нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Генерация QR-кодов и их статусов
    codes_dict = generate_qr_codes(num_codes, output_folder)

    # Создание Excel файла
    create_excel(codes_dict, output_folder)
    print(
        f"Генерация завершена. QR коды и таблица сохранены в папке {output_folder}")


if __name__ == "__main__":
    main()

