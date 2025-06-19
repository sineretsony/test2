import numpy as np
import tifffile
import os

desktop = os.path.expandvars(r"%USERPROFILE%\Desktop\Новая папка")

patterns = {
    "FOIL-": "FT-",
    "VARNISH-": "VT-",
    "FOIL_GOLD-": "FGT-",
    "FOIL_SILVER-": "FST-",
}


def find_pairs(folder):
    files = os.listdir(folder)
    pairs = []
    for base_prefix, mask_prefix in patterns.items():
        base_files = [f for f in files if f.startswith(base_prefix) and f.lower().endswith(".tif")]
        for base_file in base_files:
            suffix = base_file[len(base_prefix):]
            mask_file = f"{mask_prefix}{suffix}"
            if mask_file in files:
                pairs.append((base_file, mask_file))
    return pairs


def pixels_to_mm(pixels, dpi):
    inches = pixels / dpi
    mm = inches * 25.4
    return mm


pairs = find_pairs(desktop)

for base_file, mask_file in pairs:
    base_path = os.path.join(desktop, base_file)
    mask_path = os.path.join(desktop, mask_file)
    result_name = base_file.rsplit('.', 1)[0] + "_result.tif"
    result_path = os.path.join(desktop, result_name)

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

    # Поворот результата на 90° по часовой
    combined_rotated = np.rot90(combined, k=3)

    # Размер в пикселях после поворота
    height_px, width_px = combined_rotated.shape[:2]

    # Целевые PPI
    dpi = 360

    # Запись с указанным DPI
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

    # Расчёт финальных размеров
    width_mm = pixels_to_mm(width_px, dpi)
    height_mm = pixels_to_mm(height_px, dpi)

    print(f"Создан файл: {result_name}")
    print(f"Размер в пикселях: {width_px} x {height_px}")
    print(f"Физический размер @360ppi: {width_mm:.2f} x {height_mm:.2f} мм")

    os.remove(base_path)
    os.remove(mask_path)
    print(f"Удалены: {base_file}, {mask_file}")
