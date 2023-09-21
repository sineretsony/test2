import os
import shutil
import re
import tkinter as tk
from tkinter import filedialog
import time


def extract_first_number(name):
    match = re.search(r'\d+', name)
    if match:
        return int(match.group())
    return 0


def copy_files_with_new_names(path1, path2):
    for original_name in os.listdir(path1):
        first_number = extract_first_number(original_name)
        if first_number == 0:
            continue

        base_name, extension = os.path.splitext(original_name)
        original_path = os.path.join(path1, original_name)

        # Create a dictionary to store the new file names and their paths
        new_files = {}

        for counter in range(1, first_number + 1):
            new_name = f"{base_name}_{counter:03d}{extension}"
            new_path = os.path.join(path2, new_name)
            new_files[new_path] = original_path

        # Copy all the files at once without any delay
        for new_path, original_path in new_files.items():
            shutil.copy(original_path, new_path)


# def copy_files_with_new_names(path1, path2):
#     for original_name in os.listdir(path1):
#         first_number = extract_first_number(original_name)
#         if first_number == 0:
#             continue
#
#         base_name, extension = os.path.splitext(original_name)
#         original_path = os.path.join(path1, original_name)
#
#         for counter in range(1, first_number + 1):
#             new_name = f"{base_name}_{counter:03d}{extension}"
#             new_path = os.path.join(path2, new_name)
#             shutil.copy(original_path, new_path)
#
#             time.sleep(0.01)


def select_source_folder():
    global source_path
    source_path = filedialog.askdirectory()
    source_path_label.config(text=f"Source Folder: {source_path}")


def select_destination_folder():
    global destination_path
    destination_path = filedialog.askdirectory()
    destination_path_label.config(
        text=f"Destination Folder: {destination_path}")


def copy_files():
    if source_path and destination_path:
        copy_files_with_new_names(source_path, destination_path)
        status_label.config(text="Copying files completed.")
    else:
        status_label.config(
            text="Please select source and destination folders.")


app = tk.Tk()
app.geometry('400x220')
app.resizable(False, False)
app.title('File Copy Utility')

source_path = ''
destination_path = ''

source_btn = tk.Button(app, text="Select Source Folder",
                       command=select_source_folder)
source_btn.pack(pady=10)

source_path_label = tk.Label(app, text="Source Folder: ")
source_path_label.pack()

destination_btn = tk.Button(app, text="Select Destination Folder",
                            command=select_destination_folder)
destination_btn.pack(pady=10)

destination_path_label = tk.Label(app, text="Destination Folder: ")
destination_path_label.pack()

copy_btn = tk.Button(app, text="Copy Files", command=copy_files)
copy_btn.pack(pady=20)

status_label = tk.Label(app, text="")
status_label.pack()

app.mainloop()
