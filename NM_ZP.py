import pandas as pd

# Загружаем данные из Excel
file_path = r'C:\Users\gorea\Desktop\typography_order_product_production_operations_2025-02-01_15_22_44.xlsx'
excel_data = pd.read_excel(file_path)

# Инициализируем словарь для хранения данных
result_dict = {}

# Проходим по каждой строке таблицы
for _, row in excel_data.iterrows():
    assignee = row['assignee']  # Извлекаем Имя и Фамилию
    task = row[
        'task']  # Извлекаем тип операции (например, "Спуск полос", "Проверка макета")

    # Если сотрудника нет в словаре, добавляем его
    if assignee not in result_dict:
        result_dict[assignee] = {}

    # Если тип операции нет в подсловаре сотрудника, добавляем его с начальным значением 0
    if task not in result_dict[assignee]:
        result_dict[assignee][task] = 0

    # Увеличиваем счётчик для этой операции
    result_dict[assignee][task] += 1

# Выводим результат
for assignee, operations in result_dict.items():
    print(f'{assignee}:')
    for operation, count in operations.items():
        print(f'  {operation}: {count}')
