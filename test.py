import tkinter as tk
from tkinter import filedialog
from psd_tools import PSDImage
import os


def choose_folder():
    folder_path = filedialog.askdirectory()
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.psd'):
            psd_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-4] + '.pdf'
            pdf_file_path = os.path.join(folder_path, pdf_file_name)
            with open(pdf_file_path, 'wb') as f:
                PSDImage.open(psd_file_path).composite().save(f)
        elif file_name.endswith('.ai'):
            ai_file_path = os.path.join(folder_path, file_name)
            pdf_file_name = file_name[:-3] + '.pdf'
            pdf_file_path = os.path.join(folder_path, pdf_file_name)
            os.rename(ai_file_path, pdf_file_path)


root = tk.Tk()
button = tk.Button(root, text='Open File', command=choose_folder)
button.pack()
root.mainloop()
