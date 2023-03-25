import tkinter as tk
from tkinter import filedialog
from psd_tools import PSDImage
import os
import shutil


def browse_folder():
    global count
    count = 0
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_button.config(state=tk.NORMAL)
        path_var.set(folder_path)
        count_var.set(f'Files: {count}')


def convert_folder():
    global count
    folder_path = path_var.get()
    count = 0
    results_dir = os.path.join(folder_path, 'results')
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    psd_selected = psd_var.get()
    ai_selected = ai_var.get()

    for file_name in os.listdir(folder_path):
        if psd_selected and file_name.endswith('.psd'):
            psd_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-4] + '.pdf'
            pdf_file_path = os.path.join(results_dir, pdf_file_name)
            with open(pdf_file_path, 'wb') as f:
                PSDImage.open(psd_file_path).composite().save(f)
                count += 1
        elif ai_selected and file_name.endswith('.ai'):
            ai_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-3] + '.pdf'
            pdf_file_path = os.path.join(results_dir, pdf_file_name)
            shutil.copyfile(ai_file_path, pdf_file_path)
            count += 1

    count_var.set(f'Files: {count}')
    result_window = tk.Toplevel(root)
    result_window.title('result')
    result_window.geometry('100x60')
    tk.Label(result_window, text='done').pack()
    tk.Button(result_window, text='Ok', command=result_window.destroy).pack()


root = tk.Tk()
root.geometry('190x220')
root.resizable(False, False)
root.title('Linsh')

path_var = tk.StringVar()
psd_var = tk.BooleanVar()
ai_var = tk.BooleanVar()
count_var = tk.StringVar()

psd_checkbox = tk.Checkbutton(root, text='PSD', variable=psd_var)
ai_checkbox = tk.Checkbutton(root, text='AI', variable=ai_var)

psd_checkbox.place(x=115, y=60)
ai_checkbox.place(x=36, y=60)

browse_button = tk.Button(root, text='Browse', command=browse_folder)
browse_button.place(x=36, y=110)

convert_button = tk.Button(root, text='Start', state=tk.DISABLED, command=convert_folder)
convert_button.place(x=115, y=110)

count_label = tk.Label(root, textvariable=count_var)
count_label.place(x=90, y=170, relwidth=1, anchor='center')

footer_label = tk.Label(root, text="Made by Gregoire for Printoriny 2023", font=('Arial', 7))
footer_label.pack(side=tk.BOTTOM, pady=5)

info_label = tk.Label(root, text="Choose a format, folder \nand start the conversion", font=('Arial', 9))
info_label.pack(side=tk.TOP, pady=12)

root.mainloop()
