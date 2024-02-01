import json
import tkinter as tk
from tkinter import ttk

file_path = 'base.json'
new_data = {'KONIKA c6085 4+0': 'c6085 4+0'}


def start_app(f_path):
    try:
        with open(f_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


def save_new_data(data, n_data):
    data.update(n_data)
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def generate_name(a, b):
    return f'{a} + {b}'



class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Алгоритм druk editor")
        self.root.resizable(False, False)
        self.root.geometry('850x200')

        # Frame for copying text
        self.copy_frame = ttk.Frame(root)
        self.copy_frame.pack(pady=10)
        self.copy_text = tk.Text(self.copy_frame, height=1, state='disabled', wrap='none')
        self.copy_text.pack(side='left')
        copy_button = ttk.Button(self.copy_frame, text="Copy", command=self.copy_text_value)
        copy_button.pack(side='left', padx=5)

        # Frame for adding key-value pair
        self.add_frame = ttk.Frame(root)
        self.add_frame.pack(pady=10)

        self.key_var = tk.StringVar()
        key_label = ttk.Label(self.add_frame, text="Выбрать операцию:")
        key_label.grid(row=0, column=0, padx=5)
        self.key_dropdown = ttk.Combobox(self.add_frame, textvariable=self.key_var, width=85)
        self.key_dropdown.grid(row=0, column=1, padx=5)
        self.key_dropdown['values'] = list(info_data.keys())

        add_button = ttk.Button(self.add_frame, text="Добавить", command=self.add_value_to_copy)
        add_button.grid(row=0, column=2, padx=5)

        # Frame for creating new key-value pair
        self.create_frame = ttk.Frame(root)
        self.create_frame.pack(pady=10)

        name_label = ttk.Label(self.create_frame, text="Имя-описание:")
        name_label.grid(row=0, column=0, padx=5)
        self.name_entry = ttk.Entry(self.create_frame)
        self.name_entry.grid(row=0, column=1, padx=5)

        value_label = ttk.Label(self.create_frame, text="Значение:")
        value_label.grid(row=0, column=2, padx=5)
        self.value_entry = ttk.Entry(self.create_frame)
        self.value_entry.grid(row=0, column=3, padx=5)

        create_button = ttk.Button(self.create_frame, text="Создать", command=self.create_new_key_value)
        create_button.grid(row=0, column=4, padx=5)

    def copy_text_value(self):
        value_to_copy = self.copy_text.get("1.0", tk.END)
        self.copy_text.config(state='normal')
        self.copy_text.clipboard_clear()  # очистить буфер обмена
        self.copy_text.clipboard_append(value_to_copy)  # добавить текст в буфер обмена
        self.copy_text.delete(1.0, tk.END)  # очистить содержимое Text виджета
        self.copy_text.config(state='disabled')

    def add_value_to_copy(self):
        selected_key = self.key_var.get()
        if selected_key:
            current_text = self.copy_text.get(1.0, tk.END).strip()
            new_value = info_data[selected_key]
            if current_text:
                new_text = f"{current_text} + {new_value}"
            else:
                new_text = new_value
            self.copy_text.config(state='normal')
            self.copy_text.delete(1.0, tk.END)
            self.copy_text.insert(tk.END, new_text)
            self.copy_text.config(state='disabled')

    def create_new_key_value(self):
        new_name = self.name_entry.get()
        new_value = self.value_entry.get()
        if new_name and new_value:
            new_data = {new_name: new_value}
            save_new_data(info_data, new_data)
            self.key_dropdown['values'] = list(info_data.keys())
            self.name_entry.delete(0, tk.END)
            self.value_entry.delete(0, tk.END)


if __name__ == "__main__":
    info_data = start_app(file_path)

    root = tk.Tk()
    app = App(root)
    root.mainloop()

# pyinstaller -F -w -i C:\Users\gorea\PycharmProjects\pythonProject5\Panda-Christmas.ico ALGO.py