import subprocess
import tkinter as tk
from tkinter import filedialog
from psd_tools import PSDImage
import os
import shutil
from datetime import datetime


def browse_folder():
    global count
    count = 0
    folder_path = filedialog.askdirectory()
    if folder_path:
        convert_button.config(state=tk.NORMAL)
        fast_ai.config(state=tk.NORMAL)
        path_var.set(folder_path)


def is_date_valid(date_str, button, button2):
    date = datetime.strptime(date_str, '%d.%m.%Y')
    if date > datetime.now():
        button.configure(state=tk.NORMAL)
        button2.configure(state=tk.DISABLED)
    else:
        button.configure(state=tk.DISABLED)
        button2.configure(state=tk.NORMAL)


def caesar_decrypt_from_file():
        filename = 'data.sh'
        if os.path.isfile(filename) and os.path.getsize(filename) > 0:
            created_time = datetime.fromtimestamp(
                os.path.getctime(filename)).date()
            modified_time = datetime.fromtimestamp(
                os.path.getmtime(filename)).date()
            if created_time != modified_time:
                return '22.01.1900'
            with open(filename, 'rb') as file:
                data = file.read()
                decoded_data = data.decode('utf-8')
            slice_1 = 0
            slice_2 = 9
            result = ""
            count = 0
            for k in decoded_data:
                count += 1
                if count == 3 or count == 7:
                    slice_1 += 9
                    slice_2 += 9
                result += chr((ord(k) - (slice_1 + slice_2)) % 256)
            if len(result) != 10:
                return '22.01.1900'
            return result
        else:
            return '22.01.1900'


def register_window():
    def register():
        text = entry.get()
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                               'data.sh'), 'wb') as file:
            file.write(text.encode('utf-8'))
        root.destroy()

    root = tk.Tk()
    root.geometry('200x50')

    entry = tk.Entry(root, width=20)
    entry.pack(pady=5)

    button = tk.Button(root, text='Save to file', command=register)
    button.pack()

    root.mainloop()


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


def fast_ai_conversion():
    folder_path = path_var.get()
    if os.path.exists(folder_path):
        os.chdir(folder_path)
        command = "ren *.ai *.pdf"
        result = subprocess.run(command, shell=True)
        count = len([f for f in os.listdir(folder_path) if f.endswith('.pdf')])
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


color = '#ffffff'
text_color = '#000000'
font, size = 'Arial', 9

root = tk.Tk()
root.geometry('190x220')
root.resizable(False, False)
root.title('ufo conv')
root.attributes('-toolwindow', True)
root.tk_setPalette(background=color)
root.configure(bg=color, highlightbackground=color, highlightcolor=color)

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()

center_x = int(screen_width / 4)
center_y = int(screen_height / 4)

root.geometry(f'+{center_x}+{center_y}')

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
                          fg='#007015', bg=color, state=tk.DISABLED, width=7,
                          height=2, command=browse_folder)
browse_button.place(x=32, y=85)

convert_button = tk.Button(root, text='Start', font=(font, size, 'bold'),
                           fg='#A32E00', bg=color, state=tk.DISABLED, width=7,
                           height=2, command=convert_folder)
convert_button.place(x=102, y=85)

fast_ai = tk.Button(root, text='FAST AI', font=(font, size, 'bold'),
                    fg='#000DFF', bg=color, state=tk.DISABLED, width=7,
                    height=2, command=fast_ai_conversion)
fast_ai.place(x=32, y=135)

license_button = tk.Button(root, text='License', font=(font, size, 'bold'),
                           fg='#A32E00', bg=color, width=7,
                           height=2, command=register_window)
license_button.place(x=102, y=135)

info_label = tk.Label(root, text="Choose a format, folder \n "
                                 "and start the conversion",
                      fg=text_color, bg=color, font=(font, 9, 'bold'))
info_label.pack(side=tk.TOP, pady=12)

footer_label = tk.Label(root, text="Made by Gregoire 2023",
                        fg=text_color, bg=color, font=(font, 7))
footer_label.pack(side=tk.BOTTOM, pady=5)

is_date_valid(caesar_decrypt_from_file(), browse_button, license_button)
root.mainloop()

#шифр и дешифр

# # Исходная дата
# date = '10.04.2100'
#
# # Ключ шифрования
# key = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tempor ' \
#       'at ex in pharetra. Etiam a elit at ex pharetra semper.'
#
#
# # Функция для шифрования
# def caesar(n):
#     temp = ""
#     slice_1 = 0
#     slice_2 = 9
#     count = 0
#     for i in n:
#         count += 1
#         if count == 3 or count == 7:
#             slice_1 += 9
#             slice_2 += 9
#         temp += chr((ord(i) + (slice_1 + slice_2)) % 256)
#     return temp
#
#
# z = caesar(date)
# print(z)
#
#
# def caesar_decrypt(s):
#     slice_1 = 0
#     slice_2 = 9
#     result = ""
#     count = 0
#     for i in s:
#         count += 1
#         if count == 3 or count == 7:
#             slice_1 += 9
#             slice_2 += 9
#         result += chr((ord(i) - (slice_1 + slice_2)) % 256)
#     return result
#
#
# print(caesar_decrypt(z))


