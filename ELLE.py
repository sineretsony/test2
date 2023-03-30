import subprocess
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
        fast_ai.config(state=tk.NORMAL)
        path_var.set(folder_path)


def fast_ai_conversion():
    folder_path = path_var.get()
    if os.path.exists(folder_path):
        os.chdir(folder_path)
        command = "ren *.ai *.pdf"
        result = subprocess.run(command, shell=True)
        count = len([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
        window_results()


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

    window_results()


def window_results():
    result_window = tk.Toplevel(root)
    result_window.title('result')
    result_window.geometry('150x60')

    screen_width = result_window.winfo_screenwidth()
    screen_height = result_window.winfo_screenheight()

    result_window.update_idletasks()
    window_width = result_window.winfo_width()
    window_height = result_window.winfo_height()

    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    result_window.geometry(
        '{}x{}+{}+{}'.format(window_width, window_height, x, y))
    result_window.attributes('-toolwindow', True)
    result_window.resizable(False, False)

    tk.Label(result_window, text=f'Convert: {count} files').pack()
    tk.Button(result_window, text='Ok',
              command=result_window.destroy).pack()


color = '#FFFFFF'
text_color = '#000000'
font, size = 'Arial', 9

root = tk.Tk()
root.geometry('190x220')
root.resizable(False, False)
root.title('Guinea conv')
root.attributes('-toolwindow', True)
root.configure(bg=color)

path_var = tk.StringVar()
psd_var = tk.BooleanVar(value=True)
ai_var = tk.BooleanVar(value=True)
count_var = tk.StringVar()

psd_checkbox = tk.Checkbutton(root, text='PSD', font=(font, size, 'bold'),
                              fg=text_color, bg=color, variable=psd_var)
ai_checkbox = tk.Checkbutton(root, text='AI', font=(font, size, 'bold'),
                             fg=text_color, bg=color, variable=ai_var)

psd_checkbox.place(x=102, y=50)
ai_checkbox.place(x=28, y=50)

browse_button = tk.Button(root, text='Open', font=(font, size, 'bold'),
                          fg='#007015', bg=color, width=7,
                          height=2, command=browse_folder)
browse_button.place(x=32, y=85)

convert_button = tk.Button(root, text='Start', font=(font, size, 'bold'),
                           fg='#A32E00', bg=color, state=tk.DISABLED, width=7,
                           height=2, command=convert_folder)
convert_button.place(x=102, y=85)

fast_ai = tk.Button(root, text='FAST CONV AI', font=(font, size, 'bold'),
                    fg='#CD00D8', bg=color, state=tk.DISABLED, width=17,
                    height=2, command=fast_ai_conversion)
fast_ai.place(x=32, y=135)

info_label = tk.Label(root, text="Choose a format, folder \n "
                                 "and start the conversion",
                      fg=text_color, bg=color, font=(font, 9, 'bold'))
info_label.pack(side=tk.TOP, pady=12)

footer_label = tk.Label(root, text="Made by Gregoire 2023",
                        fg=text_color, bg=color, font=(font, 7))
footer_label.pack(side=tk.BOTTOM, pady=5)

root.mainloop()
