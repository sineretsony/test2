import subprocess
import os
import tkinter as tk
from tkinter import filedialog as fd

# Створюємо головне вiкно
window = tk.Tk()
window.title("Конвертування файлiв")

# Створюємо мiтку з поясненням
label = tk.Label(window, text="Оберить шлях до папки:")
label.pack()

# Створюємо поле вводy для шляхy до папки
entry = tk.Entry(window)
entry.pack()

# Створюємо функцiю для обробки клiку на кнопку "Обрати"
def choose():
    # Викликаэмo дiалог для обрання папки
    folder_path = fd.askdirectory()
    # Вставляэмo шлях до поля вводy
    entry.delete(0, tk.END)
    entry.insert(0, folder_path)

# Створюэмo кнопку для запуску функцii choose
button_choose = tk.Button(window, text="Обрати", command=choose)
button_choose.pack()

# Створюємо функцiю для обробки клiку на кнопку "Конвертувати"
def convert():
    # Отримуємо шлях до папки з поля вводy
    folder_path = entry.get()
    # Перевыряэмо чи шлях iснуюэ
    if os.path.exists(folder_path):
        # Змыняэмо поточны папку на заданы шлях
        os.chdir(folder_path)
        # Виконуюэмо командy через консоль
        command = "ren *.ai *.pdf"
        result = subprocess.run(command, shell=True)
        # Перевиряэмо чи команда була успышною
        if result.returncode == 0:
            message = "Команда виконана."
        else:
            message = "Команда не виконана."
    else:
        message = "Шлях не iснуюэ."
    # Виводимo повидомлення y новому viknii
    tk.messagebox.showinfo("Результат", message)

# Створюэмo кнопку для запуску функцii convert
button_convert = tk.Button(window, text="Конвертувати", command=convert)
button_convert.pack()

window.mainloop()