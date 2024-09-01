import os
import shutil
import time
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox


def get_versioned_filename(path, filename):
    base_name, ext = os.path.splitext(filename)
    version = 1
    while os.path.exists(os.path.join(path, f"v{version}_{base_name}{ext}")):
        version += 1
    return f"v{version}_{base_name}{ext}"


def monitor_directory(source_dir, backup_dir):
    files_data = {}

    while True:
        for filename in os.listdir(source_dir):
            source_path = os.path.join(source_dir, filename)
            if os.path.isfile(source_path):
                file_stat = os.stat(source_path)
                last_modified_time = file_stat.st_mtime

                if filename not in files_data or files_data[
                    filename] != last_modified_time:
                    files_data[filename] = last_modified_time

                    # Создаем папку с текущей датой
                    date_folder = datetime.now().strftime("%Y_%m_%d")
                    target_path = os.path.join(backup_dir, date_folder)
                    os.makedirs(target_path, exist_ok=True)

                    # Генерируем версионное имя файла внутри этой папки
                    versioned_filename = get_versioned_filename(target_path,
                                                                filename)

                    # Копируем файл с версионным именем
                    shutil.copy2(source_path,
                                 os.path.join(target_path, versioned_filename))
                    print(
                        f"Скопировано: {source_path} -> {os.path.join(target_path, versioned_filename)}")

        time.sleep(10)  # Проверка каждые 10 секунд


def start_monitoring(source_dir, backup_dir):
    if not source_dir or not backup_dir:
        messagebox.showwarning("Ошибка", "Пожалуйста, выберите обе папки!")
        return
    monitor_directory(source_dir, backup_dir)


def select_source_dir():
    source_dir.set(filedialog.askdirectory())


def select_backup_dir():
    backup_dir.set(filedialog.askdirectory())


if __name__ == "__main__":
    # Создаем главное окно
    root = tk.Tk()
    root.title("Copyfay")

    source_dir = tk.StringVar()
    backup_dir = tk.StringVar()

    # Создаем элементы интерфейса
    tk.Label(root, text="Папка для отслеживания:").grid(row=0, column=0,
                                                        padx=10, pady=5)
    tk.Entry(root, textvariable=source_dir, width=50).grid(row=0, column=1,
                                                           padx=10, pady=5)
    tk.Button(root, text="Выбрать...", command=select_source_dir).grid(row=0,
                                                                       column=2,
                                                                       padx=10,
                                                                       pady=5)

    tk.Label(root, text="Папка для копий:").grid(row=1, column=0, padx=10,
                                                 pady=5)
    tk.Entry(root, textvariable=backup_dir, width=50).grid(row=1, column=1,
                                                           padx=10, pady=5)
    tk.Button(root, text="Выбрать...", command=select_backup_dir).grid(row=1,
                                                                       column=2,
                                                                       padx=10,
                                                                       pady=5)

    tk.Button(root, text="Начать мониторинг",
              command=lambda: start_monitoring(source_dir.get(),
                                               backup_dir.get())).grid(row=2,
                                                                       column=1,
                                                                       padx=10,
                                                                       pady=20)

    # Запуск интерфейса
    root.mainloop()
