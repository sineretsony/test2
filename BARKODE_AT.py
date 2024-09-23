import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from pathlib import Path
import reportlab
from reportlab.graphics import renderPDF
from reportlab.pdfgen import canvas
from reportlab.graphics.barcode import eanbc
from reportlab.graphics.shapes import Drawing
from reportlab.lib.units import mm
import time
import json

ACTIVATION_FILE = 'activation.json'

def check_activation():
    """Проверка, активирована ли программа."""
    if not os.path.exists(ACTIVATION_FILE):
        return False

    with open(ACTIVATION_FILE, 'r') as file:
        data = json.load(file)
        activation_code = data.get("activation_code", "")

    # Удаляем все символы, которые не являются цифрами
    activation_code = ''.join(filter(str.isdigit, activation_code))

    # Проверяем, что после удаления остались цифры
    if not activation_code:
        return False

    # Подсчет суммы цифр
    total_sum = sum(int(digit) for digit in activation_code)

    if total_sum == 103:
        return True
    else:
        return False


def start_activation():
    """Запуск программы активации в свернутом виде."""
    # Запуск activation.py в новом процессе и в свернутом виде
    subprocess.Popen(['python', 'activation.py'], creationflags=subprocess.CREATE_NEW_CONSOLE)

def wait_for_activation():
    """Ожидание завершения активации."""
    print("Ожидание активации...")
    while not check_activation():
        time.sleep(3)  # Ожидание 3 секунды перед проверкой снова
    print("Активация завершена.")

def start_barcode_program():
    """Основная логика программы после активации."""


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
        file_path = tk.filedialog.askopenfilename(title="Выберите файл",
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

    root = tk.Tk()
    root.title("Barcode Generator")
    root.geometry("300x150")

    open_button = tk.Button(root, text="Выбрать файл", command=open_file)
    open_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    start_activation()
    time.sleep(3)
    if check_activation():
        start_barcode_program()
    else:
        wait_for_activation()  # Ожидание успешной активации
        print("Запуск программы после активации.")
        start_barcode_program()
