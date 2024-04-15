import os
from pathlib import Path
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import mm


def createBarCodes(value, count):
    desktop_path = Path(os.path.expanduser("~/Desktop/barcodeks"))

    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    file_path = desktop_path / f"{count}_{value}.pdf" # путь для сохранения
    c = canvas.Canvas(str(file_path), pagesize=(37 * mm, 28 * mm))
    barcode_eanbc = eanbc.Ean13BarcodeWidget(value)
    d = Drawing(50, 10)
    d.add(barcode_eanbc)
    renderPDF.draw(d, c, 1 * mm, 1 * mm)
    c.save()


def plays_app(barcode_data):
    data_spl = barcode_data.strip().split('\n')
    count = 0
    final = 0
    for code in data_spl:
        try:
            createBarCodes(code, f'{count:003}')
            print(f'Код {code} успешно сгенерирован')
            final += 1
        except:
            print(f'Произошла ошибка генерации кода {code}')
        count += 1
    print(f'Кодов сгенерировано {final} из {count}')
    input('Нажмите любую кнопку для выхода или закройте окно..')

try:
    with open('BKS.txt', 'r', encoding='utf-8') as file:
        date = file.read()
        plays_app(date)
except:
    print('Текстовый файл BKS.txt не найден или пустой')
    input('')

# pyinstaller -F -i C:\Users\gorea\PycharmProjects\pythonProject5\Iconka-Cat-Halloween-Cat-ghost.ico BARCODEKS.py