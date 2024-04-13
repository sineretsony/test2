import os
from pathlib import Path

from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape, A4
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import mm


def createBarCodes(value, count):
    desktop_path = Path(os.path.expanduser("~/Desktop"))
    file_path = desktop_path / f"{count}_{value}.pdf" # путь для сохранения
    c = canvas.Canvas(str(file_path), pagesize=(37 * mm, 28 * mm))
    barcode_eanbc = eanbc.Ean13BarcodeWidget(value)
    d = Drawing(50, 10)
    d.add(barcode_eanbc)
    renderPDF.draw(d, c, 1 * mm, 1 * mm)
    c.save()


def plays_app(barcode_data):
    data_spl = barcode_data.strip().split('\n')
    count = 1
    for code in data_spl:
        createBarCodes(code, f'{count:003}')
        count += 1


date = '''
4820218797921
4820218797983
'''
plays_app(date)
