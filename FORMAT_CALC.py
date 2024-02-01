import tkinter as tk
from tkinter import ttk


def get_number_in_name(s):
    w = ''
    temp = ''
    for i in s:
        if i.isdigit():
            temp += i
        if i == 'x':
            w = temp
            temp = ''
    h = temp
    return int(w), int(h)


def calc_width(mac_size_w, mac_size_h, x, y):
    cal1 = x // mac_size_w
    cal2 = y // mac_size_h
    cal3 = cal1 * cal2

    cal4 = y // mac_size_w
    cal5 = x // mac_size_h
    cal6 = cal4 * cal5

    if cal3 > cal6:
        return cal3
    else:
        return cal6

def calculate_width():
    width = int(entry_width.get())
    height = int(entry_height.get())

    selected_format = format_combobox.get()
    format_width, format_height = get_number_in_name(selected_format)

    if manual_cut_var.get():
        format_width -= 4
        format_height -= 4
        print('минус')

    bleed = 2
    x = format_width
    y = format_height

    w = width + bleed + bleed
    h = height + bleed + bleed

    result = calc_width(w, h, x, y)

    result_label.config(text=f'Макетов ложится: {result}')



def clear_values():
    entry_width.delete(0, tk.END)
    entry_height.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.resizable(False, False)
root.title("Расчет количества")

manual_cut_var = tk.BooleanVar(value=False)  # Переменная для чекбокса "ручная порезка"
manual_cut_checkbox = tk.Checkbutton(root, text="Ручная порезка", variable=manual_cut_var)
manual_cut_checkbox.grid(row=3, column=2, padx=10, pady=10)

formats = ["F-MARK 440x295", "F-MARK MGI 429x286", "IECHO 286x480", "KONIKA 320x480", "КОНВЕРТ ЛАМ 301x415", "BANNER 690x320", "MAGNIT 306x476"]  # Добавьте свои форматы
format_combobox = ttk.Combobox(root, values=formats)
format_combobox.set(formats[0])  # Устанавливаем значение по умолчанию
format_combobox.grid(row=2, column=1, padx=10, pady=10)

label_width = tk.Label(root, text="Ширина макета мм:")
label_width.grid(row=0, column=0, padx=10, pady=10)

entry_width = tk.Entry(root)
entry_width.grid(row=0, column=1, padx=10, pady=10)

label_height = tk.Label(root, text="Высота макета мм:")
label_height.grid(row=1, column=0, padx=10, pady=10)

entry_height = tk.Entry(root)
entry_height.grid(row=1, column=1, padx=10, pady=10)

# Добавление выпадающего списка
label_format = tk.Label(root, text="Формат:")
label_format.grid(row=2, column=0, padx=10, pady=10)

clear_button = tk.Button(root, text="Очистить", command=clear_values)
clear_button.grid(row=3, column=0, padx=10, pady=10)

calculate_button = tk.Button(root, text="Рассчитать", command=calculate_width)
calculate_button.grid(row=3, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()

#pyinstaller -F -w -i C:\Users\gorea\PycharmProjects\pythonProject5\icoico.ico FORMAT_CALC.py