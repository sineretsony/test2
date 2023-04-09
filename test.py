import os
from tkinter import *
from tkinter import filedialog

root = Tk()
root.withdraw()

# выбираем папку, в которой находятся файлы
folder_selected = filedialog.askdirectory()

# получаем название папки
folder_name = os.path.basename(folder_selected)

# создаем текстовый документ с названием папки
with open(folder_name + ".txt", "w") as file:

    # считываем названия файлов и записываем их в текстовый документ
    for filename in os.listdir(folder_selected):
        file.write(filename + "\n")
