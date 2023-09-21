# import svgwrite
#
# text = "MP_106982_5_202_297_8_7				".strip()
# print(text)
#
# temp_stack = []
# temp = ""
#
# for i in text:
#     if i != "_":
#         temp += i
#     elif i == "_":
#         temp_stack.append(temp)
#         temp = ""
#
# temp_stack.append(temp)
# print(temp_stack)
#
# type_pp = temp_stack[0]
#
#
# # Создаем объект Drawing с указанием размеров холста
# dwg = svgwrite.Drawing(filename=text+".svg", size=('300mm', '210mm'))
#
# # Параметры линии
# line_height = '210mm'  # Высота линии
#
# # Линия
# line = dwg.line(start=('0mm', 0), end=('0mm', line_height), stroke='black')
# line2 = dwg.line(start=('15mm', 0), end=('15mm', line_height), stroke='black')
# line3 = dwg.line(start=('150mm', 0), end=('150mm', line_height), stroke='black')
# line4 = dwg.line(start=('158mm', 0), end=('158mm', line_height), stroke='black')
# line5 = dwg.line(start=('178mm', 0), end=('178mm', line_height), stroke='black')
#
#
# # Добавляем линию в рисунок
# dwg.add(line)
# dwg.add(line2)
# dwg.add(line3)
# dwg.add(line4)
# dwg.add(line5)
#
# # Сохраняем рисунок в файл
# dwg.save()
#
import os


# filename = r'C:\Users\gorea\Desktop\Новая папка\7878.txt'
# # input_folder = r'C:\Users\gorea\Desktop\Новая папка\A4'
# # output_folder = r'C:\Users\gorea\Desktop\Новая папка\END'
# #
# # with open(filename, 'r') as file:
# #     lines = file.readlines()
# #
# # data_dict = {}
# #
# # for line in lines:
# #     line = line.strip()
# #     key, value = line.split('\t')
# #     key = key.replace('#', '')
# #     key = key.upper()
# #     value = int(value)
# #     if value != 0:
# #         data_dict[key] = value
# #
# #
# # def process_files(input_folder, output_folder):
# #     if not os.path.exists(output_folder):
# #         os.makedirs(output_folder)
# #
# #     for filename in os.listdir(input_folder):
# #         input_path = os.path.join(input_folder, filename)
# #         output_path = os.path.join(output_folder, filename)
# #         file_name, file_ext = os.path.splitext(filename)
# #         file_name = file_name.upper()
# #         if file_name in data_dict and data_dict[file_name] != 0:
# #             new_file_name = str(data_dict[file_name]) + '_' + file_name + file_ext
# #             output_path = os.path.join(output_folder, new_file_name)
# #             with open(input_path, 'rb') as input_file, open(output_path, 'wb') as output_file:
# #                 output_file.write(input_file.read())
# #
# #     print("Finish")
# #     print("Number of keys:", len(data_dict))
# #     print("Sum of all keys:", sum(data_dict.values()))
# #
# #
# # process_files(input_folder, output_folder)
# #
# # #копирование файлов с переносом последнего числа в начало
# # import os
# # import shutil
# #
# #
# # def get_last_number_in_name(name):
# #     parts = name.split()
# #     for part in reversed(parts):
# #         if part.isdigit():
# #             return int(part)
# #     return None
# #
# #
# # path1 = r"C:\Users\gorea\Desktop\001"
# # path2 = r"C:\Users\gorea\Desktop\002"
# #
# # file_dict = {}
# #
# # for filename in os.listdir(path1):
# #     filepath = os.path.join(path1, filename)
# #     if os.path.isfile(filepath):
# #         last_number = get_last_number_in_name(filename)
# #         if last_number is not None:
# #             file_dict[filename] = last_number
# #
# # for filename, value in file_dict.items():
# #     new_filename = f"{value}_{filename}"
# #     source_filepath = os.path.join(path1, filename)
# #     destination_filepath = os.path.join(path2, new_filename)
# #     shutil.copy(source_filepath, destination_filepath)

def search(m):
    tum = 0
    temp = ""
    temp_name = ""
    my_list = []
    lcl = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    for i in m:
        for j in i:
            if any(nums in j for nums in lcl):
                if tum == 2:
                    temp = ""
                temp += j
                tum = 1
            else:
                tum = 2
        if len(temp) == 0:
            temp += "!"
        temp_name = f"{temp}_{i}"
        my_list.append(temp_name)
    return my_list
