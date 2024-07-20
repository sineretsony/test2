import os
from pathlib import Path

desktop_path = Path(os.path.expanduser("~/Desktop/"))
input_file_path = os.path.join(desktop_path, 'Новый текстовый документ (2).txt')
output_file_path = os.path.join(desktop_path, 'Измененный_текстовый_документ.txt')

with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Удаление последнего символа в каждой строке и запись с новой строки
modified_lines = [line[:-2] + '\n' for line in lines if line.strip()]

with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)
