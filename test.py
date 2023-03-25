import tkinter as tk
from tkinter import filedialog
from psd_tools import PSDImage
import os
import shutil


def choose_folder():
    folder_path = filedialog.askdirectory()
    count = 0
    results_dir = os.path.join(folder_path, 'results')
    if not os.path.exists(results_dir):
        os.mkdir(results_dir)

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.psd'):
            psd_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-4] + '.pdf'
            pdf_file_path = os.path.join(results_dir, pdf_file_name)
            with open(pdf_file_path, 'wb') as f:
                PSDImage.open(psd_file_path).composite().save(f)
                count += 1
        elif file_name.endswith('.ai'):
            ai_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-3] + '.pdf'
            pdf_file_path = os.path.join(results_dir, pdf_file_name)
            shutil.copyfile(ai_file_path, pdf_file_path)
            count += 1

    result_window = tk.Toplevel(root)
    result_window.title('Результат')
    result_window.geometry('250x100')
    tk.Label(result_window, text=f'Сконвертировано {count} файлов').pack()
    tk.Button(result_window, text='OK', command=result_window.destroy).pack()


root = tk.Tk()
root.geometry('220x230')
root.resizable(False, False)
button = tk.Button(root, text='Browse', command=choose_folder)
button.pack()
root.mainloop()
