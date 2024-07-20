import os
import datetime
import win32com.client
import shutil
from pathlib import Path
import winshell
import time


def create_desktop_shortcut(link_name):
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    today = datetime.datetime.now()
    folder_name = today.strftime("%Y/%m_%B/%d_%m_%Y")
    target_path = os.path.join('M:', folder_name)
    shortcut_path = os.path.join(desktop_path, f'{link_name}.lnk')

    shell = win32com.client.Dispatch('WScript.Shell')
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.TargetPath = os.path.abspath(target_path)
    shortcut.save()


def check():
    count_sec = 0
    while True:
        if count_sec <= 0:
            count_sec = 720
            link_name = 'Shortcut'
            create_desktop_shortcut(link_name)
        count_sec -= 1
        # Путь к рабочему столу
        desktop = Path.home() / "Desktop"

        # Путь к папке PRINT на рабочем столе
        print_folder = desktop / "SORT_PRINT"

        # Если папки PRINT не существует, создаем её
        if not print_folder.exists():
            os.makedirs(print_folder)

        # Находим путь к ярлыку Shortcut на рабочем столе
        shortcut_path = winshell.shortcut(
            os.path.join(str(desktop), "Shortcut.lnk")).path

        # Получаем путь к папке PLOTTER внутри Shortcut
        plotter_folder = os.path.join(shortcut_path, "PLOTTER")
        sborka_folder = os.path.join(shortcut_path, 'SBORKA')
        lable_folder = os.path.join(shortcut_path, 'LABEL')
        mgi_folder = os.path.join(shortcut_path, 'MGI')

        # Если папки PLOTTER внутри Shortcut не существует, создаем её
        if not os.path.exists(plotter_folder):
            os.makedirs(plotter_folder)

        # Сканируем содержимое папки PRINT
        for file_name in os.listdir(print_folder):
            file_path = print_folder / file_name

            if os.path.isfile(file_path):
                if file_path.suffix == ".pdf" and 'SBORKA' not in file_path.name:
                    shutil.move(str(file_path), shortcut_path)
                    print(f'Перемещен файл печати: {file_path.name}')
                elif file_path.suffix == ".ai" or file_path.suffix == ".dxf":
                    shutil.move(str(file_path), plotter_folder)
                    print(f'Перемещен файл порезки: {file_path.name}')
                elif 'SBORKA' in file_path.name:
                    shutil.move(str(file_path), sborka_folder)
                    print(f'Перемещен файл сборки: {file_path.name}')

            elif os.path.isdir(file_path):
                has_pdf = False
                has_tif = False
                for sub_file_name in os.listdir(file_path):
                    sub_file_path = file_path / sub_file_name
                    if sub_file_path.suffix == ".pdf":
                        has_pdf = True
                    elif sub_file_path.suffix == ".tif":
                        has_tif = True
                if has_pdf:
                    shutil.move(str(file_path), lable_folder)
                    print(f'Перемещен рулонный файл: {file_path.name}')
                elif has_tif:
                    shutil.move(str(file_path), mgi_folder)
                    print(f'Перемещен MGI файл: {file_path.name}')

        # Пауза на 5 секунд перед следующей итерацией
        time.sleep(5)


try:
    check()
except Exception as e:
    print(f"An error occurred: {e}")
    input("Press Enter to exit...")
