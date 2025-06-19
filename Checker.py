import os
import datetime
import win32com.client
import shutil
from pathlib import Path
import winshell
import time
import numpy as np
import tifffile
import hashlib

def get_file_hash(filepath):
    hasher = hashlib.md5()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def process_tif_folder(folder):
    patterns = {
        "FOIL-": "FT-",
        "VARNISH-": "VT-",
        "FOIL_GOLD-": "FGT-",
        "FOIL_SILVER-": "FST-",
    }

    files = os.listdir(folder)
    pairs = []
    for base_prefix, mask_prefix in patterns.items():
        base_files = [f for f in files if f.startswith(base_prefix) and f.lower().endswith(".tif")]
        for base_file in base_files:
            suffix = base_file[len(base_prefix):]
            mask_file = f"{mask_prefix}{suffix}"
            if mask_file in files:
                pairs.append((base_file, mask_file))

    for base_file, mask_file in pairs:
        base_path = os.path.join(folder, base_file)
        mask_path = os.path.join(folder, mask_file)

        # Проверка стабильности файлов
        stable = False
        old_hash_base = old_hash_mask = None

        for _ in range(5):
            new_hash_base = get_file_hash(base_path)
            new_hash_mask = get_file_hash(mask_path)

            if new_hash_base == old_hash_base and new_hash_mask == old_hash_mask:
                stable = True
                break

            old_hash_base = new_hash_base
            old_hash_mask = new_hash_mask
            time.sleep(1.5)

        if not stable:
            print(f"Файлы {base_file} и/или {mask_file} ещё не стабильны. Пропуск.")
            continue

        result_name = base_file.rsplit('.', 1)[0] + "_result.tif"
        result_path = os.path.join(folder, result_name)

        base = tifffile.imread(base_path)
        mask = tifffile.imread(mask_path)

        if base.ndim == 3:
            base_gray = np.dot(base[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
        else:
            base_gray = base.astype(np.uint8)

        if mask.ndim == 3:
            mask_gray = np.dot(mask[..., :3], [0.299, 0.587, 0.114]).astype(np.uint8)
        else:
            mask_gray = mask.astype(np.uint8)

        min_h = min(base_gray.shape[0], mask_gray.shape[0])
        min_w = min(base_gray.shape[1], mask_gray.shape[1])
        base_gray = base_gray[:min_h, :min_w]
        mask_gray = mask_gray[:min_h, :min_w]

        combined = np.stack([base_gray, mask_gray], axis=-1)
        combined_rotated = np.rot90(combined, k=3)

        dpi = 360
        tifffile.imwrite(
            result_path,
            combined_rotated,
            photometric='minisblack',
            planarconfig='contig',
            compression='deflate',
            metadata=None,
            resolution=(dpi, dpi),
            resolutionunit='INCH'
        )

        os.remove(base_path)
        os.remove(mask_path)
        print(f"Обработан: {base_file} + {mask_file} → {result_name}")


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

        desktop = Path.home() / "Desktop"
        print_folder = desktop / "SORT_PRINT"

        if not print_folder.exists():
            os.makedirs(print_folder)

        shortcut_path = winshell.shortcut(
            os.path.join(str(desktop), "Shortcut.lnk")).path

        plotter_folder = os.path.join(shortcut_path, "PLOTTER")
        sborka_folder = os.path.join(shortcut_path, 'SBORKA')
        lable_folder = os.path.join(shortcut_path, 'LABEL')
        mgi_folder = os.path.join(shortcut_path, 'MGI')

        if not os.path.exists(plotter_folder):
            os.makedirs(plotter_folder)

        for file_name in os.listdir(print_folder):
            file_path = print_folder / file_name

            if os.path.isfile(file_path):
                if file_path.suffix == ".pdf" and 'SBORKA' not in file_path.name:
                    shutil.move(str(file_path), shortcut_path)
                    print(f'Перемещен файл печати: {file_path.name}')
                elif file_path.suffix in [".ai", ".dxf", ".eps"]:
                    shutil.move(str(file_path), plotter_folder)
                    print(f'Перемещен файл порезки: {file_path.name}')
                elif 'SBORKA' in file_path.name:
                    shutil.move(str(file_path), sborka_folder)
                    print(f'Перемещен файл сборки: {file_path.name}')

            elif os.path.isdir(file_path):
                has_pdf = any(f.suffix == ".pdf" for f in file_path.iterdir())
                has_tif = any(f.suffix == ".tif" for f in file_path.iterdir())

                if has_pdf:
                    shutil.move(str(file_path), lable_folder)
                    print(f'Перемещен рулонный файл: {file_path.name}')
                elif has_tif:
                    temp_abbr = ("VT", "FT", "FGT", "FST")
                    tif_files = [f.name for f in file_path.iterdir() if f.suffix == ".tif"]
                    if any(any(abbr in name for abbr in temp_abbr) for name in tif_files):
                        print(f"Обнаружены временные файлы в {file_path.name}, начинаю обработку...")
                        process_tif_folder(str(file_path))
                    shutil.move(str(file_path), mgi_folder)
                    print(f'Перемещен MGI файл: {file_path.name}')

        time.sleep(5)

print('Hello, welcome to Checker! v1.6')
time.sleep(1)
print('Goo...')

while True:
    try:
        check()
    except Exception as e:
        print(f'reload... {e}')
        time.sleep(60)
