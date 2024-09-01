import keyboard
import time
import mouse

def on_press(event):
    if event.name == 'n' or event.name == 'т' or mouse.is_pressed(button='middle'):
        while keyboard.is_pressed('n'):
            keyboard.press('space')
            time.sleep(0.01)  # Короткая задержка для имитации нажатия
            keyboard.release('space')
            time.sleep(0.06)  # Задержка для достижения частоты 4 нажатия в секунду

# Назначаем обработчик нажатия клавиши
keyboard.on_press(on_press)

# Бесконечный цикл для удержания программы в рабочем состоянии
keyboard.wait('esc')  # Выход из программы по нажатию клавиши 'esc'

#
# import os
# import random
# import time
# # Путь к папке с картинками
# folder_path = r'C:\Users\gorea\Desktop\Новая папка'
#
# # Получаем список файлов в папке
# files = os.listdir(folder_path)
#
# # Фильтруем только изображения (например, файлы с расширением .jpg, .png, .bmp и т.д.)
# image_files = [file for file in files if file.endswith(
#     ('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'))]
#
# # Проверяем, есть ли изображения в папке
# if not image_files:
#     print("В папке нет изображений.")
# else:
#     # Создаем словарь с названиями файлов и тремя жизнями для каждого
#     lives = {file: 3 for file in image_files}
#
#     while len(lives) > 1:
#         time.sleep(0)
#         # Выбираем случайное изображение
#         random_image = random.choice(list(lives.keys()))
#
#         # Уменьшаем количество жизней
#         lives[random_image] -= 1
#         print(
#             f"Файл {random_image} потерял жизнь. Осталось жизней: {lives[random_image]}")
#
#         # Если жизни кончились, удаляем файл из словаря
#         if lives[random_image] == 0:
#             print(f"Файл {random_image} выбыл из игры.")
#             del lives[random_image]
#
#     # Получаем оставшийся файл (победитель)
#     winner = list(lives.keys())[0]
#     print(f"Победитель: {winner}")
#
#     # Полный путь к победившему файлу
#     winner_path = os.path.join(folder_path, winner)
#
#     # Открываем победивший файл через просмотрщик Windows
#     os.startfile(winner_path)
#









