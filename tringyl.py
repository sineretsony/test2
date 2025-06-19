import os
import win32com.client
import time

# Задержка перед запуском
for i in range(1, 5):
    time.sleep(1)
    print(i)

folder_path = os.path.join(os.path.expanduser("~"), "Desktop", "Новая папка")


# Запускаем Photoshop
ps_app = win32com.client.Dispatch("Photoshop.Application")
ps_app.Visible = True  # Делаем окно Photoshop видимым

# Определяем группы файлов
prefix_pairs = {"FOIL": "FT", "VARNISH": "VT"}

for base_prefix, temp_prefix in prefix_pairs.items():
    base_files = sorted([f for f in os.listdir(folder_path) if f.startswith(base_prefix + "-") and f.endswith(".tif")])
    temp_files = sorted([f for f in os.listdir(folder_path) if f.startswith(temp_prefix + "-") and f.endswith(".tif")])

    if len(base_files) != len(temp_files):
        print(f"Ошибка: количество {base_prefix} и {temp_prefix} файлов не совпадает!")
    else:
        for base, temp in zip(base_files, temp_files):
            base_path = os.path.join(folder_path, base)
            temp_path = os.path.join(folder_path, temp)

            # Открываем основной файл (FOIL или VARNISH)
            doc = ps_app.Open(base_path)

            # Открываем временный файл (FT или VT) и копируем слой
            temp_doc = ps_app.Open(temp_path)
            temp_doc.ActiveLayer.Copy()
            temp_doc.Close()

            # Вставляем как новый слой в основной файл
            doc.Paste()

            # Выполняем экшен (имитируем нажатие F5)
            win32com.client.Dispatch("WScript.Shell").SendKeys("{F5}")
            time.sleep(3)

            # Сохраняем и закрываем
            doc.Save()
            doc.Close()

            # Удаляем временный файл
            os.remove(temp_path)

print("Готово!")