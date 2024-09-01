# import os
# import pandas as pd
#
# # Укажите путь к вашей папке
# source_folder = r'C:\Users\gorea\Desktop\3 месяц_195х75'
# destination_folder = os.path.join(source_folder, 'результат')
#
# # Создаем папку "результат", если она не существует
# if not os.path.exists(destination_folder):
#     os.makedirs(destination_folder)
#
# # Получаем список всех файлов в исходной папке
# files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
#
# # Сортируем файлы для нумерации
# files.sort()
#
# # Переименовываем и копируем файлы в новую папку, запоминаем новые имена
# new_filenames = []
# start_index = 301
# for index, filename in enumerate(files):
#     new_filename = f"{start_index + index:03d}_{filename}"
#     src_path = os.path.join(source_folder, filename)
#     dst_path = os.path.join(destination_folder, new_filename)
#     os.rename(src_path, dst_path)
#     new_filenames.append(new_filename)
#
# # Создаем DataFrame и сохраняем в Excel
# df = pd.DataFrame(new_filenames, columns=["New Filenames"])
# excel_path = os.path.join(source_folder, 'файлы_с_новыми_именами.xlsx')
# df.to_excel(excel_path, index=False)
#
# print(f"Файлы успешно переименованы и сохранены в папку: {destination_folder}")
# print(f"Таблица Excel с новыми именами файлов сохранена по пути: {excel_path}")

# import os
# import pandas as pd
#
# # Укажите путь к вашей папке с результатами
# result_folder = r'C:\Users\Designer2\Desktop\Минов\результат'
#
# # Получаем список всех файлов в папке с результатами
# files = [f for f in os.listdir(result_folder) if os.path.isfile(os.path.join(result_folder, f))]
#
# # Создаем DataFrame и сохраняем в Excel
# df = pd.DataFrame(files, columns=["Filenames"])
# excel_path = os.path.join(result_folder, 'файлы_с_именами.xlsx')
# df.to_excel(excel_path, index=False)
#
# print(f"Таблица Excel с именами файлов сохранена по пути: {excel_path}")

import keyboard

# Список строк
file_list = [
    "301_Адапттоген_посилювач_можливостей_тіла_та_мозку_3мес",
    "302_Активатор харчових добавок_БАДів_та_Регулятор_рівня_цукру_в_крові 1.0",
    "303_Активатор харчових добавок_БАДів_та_Регулятор_рівня_цукру_в_крові 2.0",
    "304_Вітамін D3 5000 UI - 3мес",
    "305_Вітамін С + Ехінацея - 3мес",
    "306_Їжовик Гребінчастий_в_капсулах_плодове_тіло_+_міцелій_3мес",
    "307_Гриб Веселка - 3мес.pdf",
    "308_Гриб Зморшок (сморчок) - 3мес.pdf",
    "309_Гриб Лисичка - 3мес.pdf",
    "310_Гриб Мейтаке - 3мес.pdf",
    "311_Гриб Рейші - 3мес.pdf",
    "312_Гриб Траметес - 3мес.pdf",
    "313_Гриб Чага - 3мес.pdf",
    "314_Гриб Шиїтаке - 3мес.pdf",
    "315_Для нервової_системи_Магній_+_Гліцин+_Вітаміни_B_3мес.pdf",
    "316_Для_зору_та_очей_Зморшок_сморчок_+_Лисичка_3мес.pdf",
    "317_Для_імунітету_3в1_Рейші_+_Шиїтаке_+_Мейтаке_3мес.pdf",
    "318_Йод + Селен + Цинк - 3мес.pdf",
    "319_Комплекс Антистрес - 3мес.pdf",
    "320_Комплекс для суглобів та хрящів кісток_Глюкозамін_+_Хондроїтин_3мес.pdf",
    "321_Комплекс натуральних екстрактів_для_жіночої_краси,_здоров’я_та_молодості (2).pdf",
    "322_Комплекс натуральних екстрактів_для_чоловічої_сили_та_здоров’я_3мес.pdf",
    "323_Кордицепс_військовий_мілітаріс_3мес.pdf",
    "324_Мікс червоного_Мухомора_+_Їжовика_Гребінчастого_50_50_3мес.pdf",
    "325_Міцелій_Їжовика_Гребінчастого_3мес.pdf",
    "326_Олія чорного кмину - 3мес.pdf",
    "327_Омега 3 - 3мес.pdf",
    "328_Плодове_тіло_Їжовика_Гребінчастого_3мес.pdf",
    "329_Спіруліна - 3мес.pdf",
    "330_Суперкомплекс грибів 10в1 - 3мес.pdf",
    "331_Хлорела - 3мес.pdf",
    "332_Червоний Мухомор - 3мес.pdf"
]

# Индекс текущего элемента в списке
current_index = 1

def insert_next_file():
    global current_index
    if current_index < len(file_list):
        # Получаем следующий файл из списка
        file_name = file_list[current_index]
        # Печатаем файл в текущем активном поле
        keyboard.write(file_name)
        # Переходим к следующему элементу в списке
        current_index += 1
    else:
        print("Список закончился!")

# Устанавливаем обработчик нажатия клавиши Tab
keyboard.add_hotkey('tab', insert_next_file)

print("Нажмите Tab для вставки следующего файла из списка...")
keyboard.wait('esc')  # Ждём нажатия клавиши Esc для выхода
