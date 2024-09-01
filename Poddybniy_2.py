import os
import tkinter as tk
from tkinter import filedialog
from rapidfuzz import fuzz
import re

window = tk.Tk()
window.geometry('250x250')

data_dict = {}


def has_different_numbers(input_str, data_dict):
    for key, value in data_dict.items():
        similarity = fuzz.ratio(input_str, key)
        numbers1 = re.findall(r'\d+', input_str)
        numbers2 = re.findall(r'\d+', key)

        # Проверяем, что схожесть достаточная и значение не равно 0
        if similarity >= 95 and value != 0:
            # Если цифры различаются, возвращаем False
            if numbers1 != numbers2:
                return False
            # Если цифры совпадают и схожесть достаточная, возвращаем True
            return True
    # Если ни одно условие не подошло, возвращаем False
    return False


def print_message(message):
    output_text.insert(tk.END, message + '\n')
    output_text.see(tk.END)


def play_button_clicked():
    input_folder_path = input_folder.get()
    output_folder_path = output_folder.get()
    file_path = file_var.get()

    if not os.path.exists(input_folder_path) or not os.path.exists(
            output_folder_path) or not os.path.exists(file_path):
        print_message("Выберите корректные пути к файлам и папкам!")
        return

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    for line in lines:
        line = line.strip()
        key, value = line.split('\t')
        key = key.replace('#', '')
        key = key.upper()
        value = int(value)
        if value != 0:
            data_dict[key] = value

    process_files(input_folder_path, output_folder_path)


def process_files(input_folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    counter = 0

    for filename in os.listdir(input_folder_path):
        input_path = os.path.join(input_folder_path, filename)
        output_path = os.path.join(output_folder_path, filename)
        file_name, file_ext = os.path.splitext(filename)
        file_name = file_name.upper()
        if has_different_numbers(file_name, data_dict):
            new_file_name = str(
                data_dict[file_name]) + '_' + file_name + file_ext
            output_path = os.path.join(output_folder_path, new_file_name)
            with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
                output_file.write(input_file.read())
                counter += 1

    print_message("Готово")
    print_message(f"Кол-во макетов: {counter} из {str(len(data_dict))}")
    print_message("Сумма колличества: " + str(sum(data_dict.values())))


def select_input_folder():
    folder_path = filedialog.askdirectory()
    input_folder.set(folder_path)


def select_output_folder():
    folder_path = filedialog.askdirectory()
    output_folder.set(folder_path)


def select_file():
    file_path = filedialog.askopenfilename()
    file_var.set(file_path)


input_folder = tk.StringVar()
output_folder = tk.StringVar()
file_var = tk.StringVar()

input_button = tk.Button(window, text="Выбрать путь к макетам",
                         command=select_input_folder)
input_button.pack()
output_button = tk.Button(window, text="Выбрать конечную папку",
                          command=select_output_folder)
output_button.pack()
file_button = tk.Button(window, text="Файл txt информационный",
                        command=select_file)
file_button.pack()
play_button = tk.Button(window, text="Play", command=play_button_clicked)
play_button.pack()
input_label = tk.Label(window, textvariable=input_folder)
input_label.pack()
output_label = tk.Label(window, textvariable=output_folder)
output_label.pack()
file_label = tk.Label(window, textvariable=file_var)
file_label.pack()

output_text = tk.Text(window, height=8, width=30)
output_text.pack()
window.mainloop()

# v 2.1