# import os
# import shutil
# import time
#
# # Указываем пути к папкам TEMP и FINAL
# temp_dir = "C:\\Users\\gorea\\PycharmProjects\\pythonProject5\\TEMP"
# final_dir = "C:\\Users\\gorea\\PycharmProjects\\pythonProject5\\FINAL"
#
# # Имя файла, в котором будем сохранять номер
# num_file = "C:\\Users\\gorea\\PycharmProjects\\pythonProject5\\last_number.txt"
#
# # Если файл с номером уже существует, считываем последний номер из него
# if os.path.exists(num_file):
#     with open(num_file, 'r') as f:
#         num = int(f.read().strip())
#
# # Задаем начальный порядковый номер
# else:
#     num = 1
#
# # Отслеживаем папку TEMP
# while True:
#     # Получаем список файлов в папке TEMP
#     files = os.listdir(temp_dir)
#
#     # Если в папке TEMP появился новый файл
#     if len(files) > 0:
#         # Получаем имя первого файла в списке
#         filename = files[0]
#
#         # Создаем новое имя файла с порядковым номером
#         new_filename = f"{num:04d}_{filename}"
#
#         # Полный путь к файлам
#         temp_file = os.path.join(temp_dir, filename)
#         final_file = os.path.join(final_dir, new_filename)
#
#         # Задержка на 5 секунд
#         time.sleep(0.5)
#
#         # Перемещаем файл в папку FINAL и нумеруем его
#         shutil.move(temp_file, final_file)
#
#         # Увеличиваем порядковый номер на 1
#         num += 1
#
#         # Сохраняем новый номер в файл
#         with open(num_file, 'w') as f:
#             f.write(str(num))

import os
import hashlib
import shutil

temp_folder = 'C:\\Users\\gorea\\Desktop\\55'
results_folder = 'C:\\Users\\gorea\\Desktop\\FINAL2'

# Создаем словарь для хранения информации о хэшах и ссылках на файлы
hash_dict = {}

# Перебираем все файлы в папке 55
for filename in os.listdir(temp_folder):
    # Проверяем, является ли файл файлом изображения
    if filename.endswith('.jpg') or filename.endswith(
            '.jpeg') or filename.endswith('.png'):
        # Считаем хэш изображения
        with open(os.path.join(temp_folder, filename), 'rb') as f:
            hash_value = hashlib.md5(f.read()).hexdigest()

        # Добавляем информацию о хэше и ссылке на файл в словарь, если хэша еще нет в словаре
        if hash_value not in hash_dict:
            hash_dict[hash_value] = os.path.join(temp_folder, filename)
        else:
            print(f"Duplicate image found: {filename}")

# Копируем все файлы из папки 55 в папку FINAL2, используя ссылки на файлы из словаря
for hash_value, filepath in hash_dict.items():
    shutil.copy2(filepath, os.path.join(results_folder, os.path.basename(filepath)))




