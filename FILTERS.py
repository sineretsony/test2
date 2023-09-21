import os
import shutil
import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def get_last_number_in_name(name):
    parts = name.split()
    last_number = None
    for part in reversed(parts):
        if any(char.isdigit() for char in part):
            last_number = part
            break
    if last_number:
        return int(''.join(filter(str.isdigit, last_number)))
    return 0


def browse_source_path():
    global path1
    path1 = Path(filedialog.askdirectory())
    source_path_var.set(path1)


def browse_destination_path():
    global path2
    path2 = Path(filedialog.askdirectory())
    destination_path_var.set(path2)


def copy_files():
    file_dict = {}

    for file_path in path1.iterdir():
        if file_path.is_file():
            filename = file_path.name
            last_number = get_last_number_in_name(filename)
            file_dict[filename] = last_number

    for filename, value in file_dict.items():
        new_filename = f"{value}_{filename}"
        source_filepath = path1 / filename
        destination_filepath = path2 / new_filename
        shutil.copy(source_filepath, destination_filepath)


app = tk.Tk()
app.geometry('190x220')
app.resizable(False, False)
app.attributes('-toolwindow', True)
app.title("File Copy Utility")

path1 = ""  # Source path
path2 = ""  # Destination path

source_path_var = tk.StringVar()
destination_path_var = tk.StringVar()

source_label = tk.Label(app, text="Source Path:")
source_label.pack()

source_entry = tk.Entry(app, textvariable=source_path_var)
source_entry.pack()

source_button = tk.Button(app, text="Browse", command=browse_source_path)
source_button.pack()

destination_label = tk.Label(app, text="Destination Path:")
destination_label.pack()

destination_entry = tk.Entry(app, textvariable=destination_path_var)
destination_entry.pack()

destination_button = tk.Button(app, text="Browse",
                               command=browse_destination_path)
destination_button.pack()

copy_button = tk.Button(app, text="Copy Files", command=copy_files)
copy_button.pack()

app.mainloop()
