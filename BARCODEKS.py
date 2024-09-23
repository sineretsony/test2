import os
from pathlib import Path
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import mm
import tkinter as tk
from tkinter import filedialog, messagebox


def createBarCodes(value, count):
    desktop_path = Path(os.path.expanduser("~/Desktop/barcod"))

    if not os.path.exists(desktop_path):
        os.makedirs(desktop_path)

    file_path = desktop_path / f"{count}_{value}.pdf"  # путь для сохранения
    c = canvas.Canvas(str(file_path), pagesize=(37 * mm, 28 * mm))
    barcode_eanbc = eanbc.Ean13BarcodeWidget(value)
    d = Drawing(50, 10)
    d.add(barcode_eanbc)
    renderPDF.draw(d, c, 1 * mm, 1 * mm)
    c.save()


def plays_app(barcode_data):
    data_spl = barcode_data.strip().split('\n')
    count = 1
    final = 1
    for code in data_spl:
        try:
            createBarCodes(code, f'{count:003}')
            print(f'Код {code} успешно сгенерирован')
            final += 1
        except Exception as e:
            print(f'Произошла ошибка генерации кода {code}: {e}')
        count += 1
    print(f'Кодов сгенерировано {final - 1} из {count - 1}')
    messagebox.showinfo("Завершено",
                        f'Кодов сгенерировано {final - 1} из {count - 1}')


def open_file():
    file_path = filedialog.askopenfilename(title="Выберите файл",
                                           filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                data = file.read()
                plays_app(data)
        except Exception as e:
            messagebox.showerror("Ошибка", f'Ошибка при чтении файла: {e}')
    else:
        messagebox.showwarning("Предупреждение", "Файл не выбран")


def main():
    root = tk.Tk()
    root.title("Barcode Generator")
    root.geometry("300x150")

    open_button = tk.Button(root, text="Выбрать файл", command=open_file)
    open_button.pack(pady=20)

    # start_button = tk.Button(root, text="Старт", command=open_file)
    # start_button.pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()

# pyinstaller -F -i C:\Users\gorea\PycharmProjects\pythonProject5\Iconka-Cat-Halloween-Cat-ghost.ico BARCODEKS.py
# pyinstaller --name BARCODEKS --onefile --icon=C:\Users\gorea\PycharmProjects\pythonProject5\Iconka-Cat-Halloween-Cat-ghost.ico --specpath . BARCODEKS.py

