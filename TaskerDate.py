import threading
import time
import re
import json
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, \
    filters
import os
import datetime
import sys


TELEGRAM_TOKEN = '6262657982:AAHEbkXHuolnojeyMXr7Sumzbz4Vmev0Lws'  #Kai
# TELEGRAM_TOKEN = '7435545228:AAGKBdDjKHn20ZuRDuAgwM768znLs-Vhk-M'  #Likhar

JSON_FILE = r"M:\setup_action_folder\orders.json"

all_orders = []

admin_id = [407170136]


def update_orders_status():
    def update_status_in_file():
        global all_orders
        json_file_path = r"M:\setup_action_folder\orders.json"

        while True:
            try:
                if os.path.exists(json_file_path):
                    with open(json_file_path, 'r', encoding='utf-8') as file:
                        orders_data = json.load(file)

                    # Удаляем старые записи
                    today = datetime.datetime.now()
                    cutoff_date = today - datetime.timedelta(days=2)

                    keys_to_delete = []
                    for order_number, order_info in orders_data.items():
                        order_date_str = order_info['date']
                        try:
                            order_date = datetime.datetime.strptime(order_date_str, '%d.%m')
                            order_date = order_date.replace(year=today.year)  # Присваиваем текущий год

                            if order_date < cutoff_date:
                                keys_to_delete.append(order_number)
                        except ValueError:
                            # Обработка случаев, если формат даты неверен
                            pass

                    for key in keys_to_delete:
                        del orders_data[key]

                    # Обновляем статус
                    for order_number in orders_data:
                        if order_number in all_orders:
                            orders_data[order_number]['file'] = 'only_file'

                    with open(json_file_path, 'w', encoding='utf-8') as file:
                        json.dump(orders_data, file, ensure_ascii=False, indent=4)

            except Exception as e:
                # Если файл занят другим приложением, ждём 2 секунды и повторяем попытку
                print(f"Ошибка: {e}")
                time.sleep(2)
                continue

            time.sleep(130)

    checker_thread = threading.Thread(target=update_status_in_file)
    checker_thread.daemon = True
    checker_thread.start()


def burnt():
    def burnt_in():
        global all_orders
        sec_numb = 0

        # Загрузка существующих заказов из файла сохранений
        save_file = 'saved_orders.json'
        if os.path.exists(save_file):
            with open(save_file, 'r', encoding='utf-8') as f:
                all_orders = json.load(f)
        else:
            all_orders = []

        while True:
            sec_numb -= 120
            sys.stdout.reconfigure(encoding='utf-8')

            def list_files_and_folders_recursive(path):
                names_list = []
                for item in os.listdir(path):
                    item_path = os.path.join(path, item)
                    if os.path.isfile(item_path):
                        names_list.append(f"{item}")
                    elif os.path.isdir(item_path):
                        names_list.append(f"{item}")
                        subfolder_names = list_files_and_folders_recursive(item_path)
                        names_list.extend(subfolder_names)
                return names_list

            today = datetime.datetime.now()
            folder_name = today.strftime("%Y/%m_%B/%d_%m_%Y")
            folder_name2 = today.strftime("%Y/%m_%B")
            if sec_numb <= 0:
                target_path = os.path.join('M:', folder_name2)
                sec_numb = 10800
            else:
                target_path = os.path.join('M:', folder_name)
            result_list = list_files_and_folders_recursive(target_path)

            for order in result_list:
                temp = order.split('_')
                num_ord = []
                cou_ord = []
                order_name = []

                for i in temp:
                    if len(num_ord) == 0:
                        if len(i) > 10:
                            continue
                        num_ord.append(i)
                    elif i.isdigit() and len(num_ord) > 0 and len(order_name) == 0:
                        cou_ord.append(i)
                    elif len(cou_ord) == 0 and '-' in i:
                        cou_ord.append(i)
                    else:
                        order_name.append(i)
                    try:
                        if len(cou_ord) > 2:
                            for temp_num in cou_ord:
                                a = f'{num_ord[0]}'
                                if a not in all_orders:
                                    all_orders.append(a)

                        elif len(cou_ord) == 1 and '-' in cou_ord[0]:
                            temp_step_orders = cou_ord[0].split('-')
                            for i in range(int(temp_step_orders[0]), int(temp_step_orders[1]) + 1):
                                if i > 1000:
                                    bb = f'{num_ord[0]}'
                                    if bb not in all_orders:
                                        all_orders.append(bb)

                        elif len(cou_ord) <= 2 and len(cou_ord) != 0:
                            for n in cou_ord:
                                if int(n) > 1000:
                                    bc = f'{num_ord[0]}'
                                    if bc not in all_orders:
                                        all_orders.append(bc)

                        elif len(num_ord) != 0:
                            if int(num_ord[0]) > 1000:
                                temp_c = f'{num_ord[0]}'
                                if temp_c not in all_orders:
                                    all_orders.append(temp_c)
                    except:
                        continue

            # Сохраняем уникальные заказы в файл
            with open(save_file, 'w', encoding='utf-8') as f:
                json.dump(all_orders, f, ensure_ascii=False, indent=4)

            time.sleep(120)

    checker_thread = threading.Thread(target=burnt_in)
    checker_thread.daemon = True
    checker_thread.start()


#-----------------------------------------------------------------------
def counter_check():
    import os
    import datetime
    import sys
    # Указываем кодировку для корректного отображения символов
    sys.stdout.reconfigure(encoding='utf-8')

    def list_files_and_folders_recursive(path):
        # Initialize an empty list to store file and folder names
        names_list = []

        # Iterate over all items in the specified path
        for item in os.listdir(path):
            # Get the full path to the item
            item_path = os.path.join(path, item)
            # Check if the item is a file or a folder
            if os.path.isfile(item_path):
                names_list.append(f"{item}")
            elif os.path.isdir(item_path):
                names_list.append(f"{item}")
                # Recursively call the function for subfolders
                subfolder_names = list_files_and_folders_recursive(item_path)
                # Add the names from subfolders to the main list
                names_list.extend(subfolder_names)

        return names_list

    # Specify the path (you can replace it with your desired path)
    desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
    today = datetime.datetime.now()
    folder_name = today.strftime("%Y/%m_%B/%d_%m_%Y")

    target_path = os.path.join('M:', folder_name)
    # target_path = r'M:\2024\08_August'

    # Get the list of file and folder names (including subfolders)
    result_list = list_files_and_folders_recursive(target_path)

    def plays_app(input_result_list):
        # NEW
        all_orders = []

        users_id = ['g', 'k', 'e', 'a']

        g = 0
        k = 0
        e = 0
        a = 0

        for order in input_result_list:
            temp = order.split('_')
            num_ord = []
            cou_ord = []
            order_name = []
            temp_users_id = ''

            # заполняем временную таблицу выше данными из имени файла
            for i in temp:

                if len(num_ord) == 0:
                    if len(i) > 10:
                        continue
                    num_ord.append(i)
                elif i in users_id and len(temp_users_id) == 0:
                    temp_users_id = i
                elif i.isdigit() and len(num_ord) > 0 and len(order_name) == 0:
                    cou_ord.append(i)
                elif len(cou_ord) == 0 and '-' in i:
                    cou_ord.append(i)
                else:
                    order_name.append(i)
                try:
                    # добавляем заказы 1_2_3_4_5
                    if len(cou_ord) > 2 and temp_users_id != '':
                        for temp_num in cou_ord:
                            a = f'{num_ord[0]}_{temp_users_id}_{temp_num}'
                            if a not in all_orders:
                                all_orders.append(a)

                    # добавляем заказы 1-19 с по какой
                    elif len(cou_ord) == 1 and '-' in cou_ord[0]:
                        temp_step_orders = cou_ord[0].split('-')
                        for i in range(int(temp_step_orders[0]), int(temp_step_orders[1]) + 1):
                            bb = f'{num_ord[0]}_{temp_users_id}_{i}'
                            if bb not in all_orders:
                                all_orders.append(bb)

                    # добавляем заказы без дробных чисел
                    elif len(cou_ord) <= 2 and len(cou_ord) != 0:
                        for n in cou_ord:
                            if temp_users_id in users_id:
                                bc = f'{num_ord[0]}_{temp_users_id}_{n}'
                                if bc not in all_orders:
                                    all_orders.append(bc)

                    elif len(num_ord) != 0 and temp_users_id in users_id:
                        temp_c = f'{num_ord[0]}_{temp_users_id}_1'
                        if temp_c not in all_orders:
                            all_orders.append(temp_c)
                except:
                    continue

        for i in all_orders:
            if 'g' in i and i[0].isdigit():
                g += 1
            elif 'k' in i and i[0].isdigit():
                k += 1
                g += 1
            elif 'e' in i and i[0].isdigit():
                e += 1
            elif 'a' in i and i[0].isdigit():
                a += 1
        return f'Гриша___{g}\n' \
               f'Ксюша___{k}❤️\n' \
               f'Женя____{e}\n' \
               f'Андрей__{a}'

    return plays_app(result_list)


def extract_info(t):
    text = t.replace(',', '.')
    order_number = re.search(r'\d+', text)
    date = re.search(r'\d{2}\.\d{2}', text)

    order_number = order_number.group(0) if order_number else "Без номера"
    date = date.group(0) if date else "Без дати"

    return order_number, date


def load_orders():
    try:
        with open(JSON_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def save_orders(orders):
    with open(JSON_FILE, 'w') as f:
        json.dump(orders, f, ensure_ascii=False, indent=4)


async def handle_message(update: Update, context):
    keyboard = [
        [KeyboardButton('Статуси замовлень ⚠️')],
        [KeyboardButton('Очистити список ❌')],
        [KeyboardButton('Допомога 🧐')]
    ]
    if update.message.from_user.id in admin_id:
        keyboard.append([KeyboardButton('DTP')])
    text = update.message.text
    print(text)
    order_number, date = extract_info(text)
    status_file = 'no_file'

    if order_number in all_orders:
        status_file = 'only_file'

    orders = load_orders()

    if text == 'Статуси замовлень ⚠️':
        status_messages = []
        for order_number, info in orders.items():
            date = info['date']
            status = info['status']
            status_file_in_js = info['file']
            if status_file_in_js == 'only_file':
                status_file = "Файл ✅"
            elif status_file_in_js == 'no_file':
                status_file = "Файл 🅾️"
            if status == 'new':
                status_text = 'Новий 🔵'
            elif status == 'not_tc':
                status_text = 'Немає ТК 🔴️'
            elif status == 'processed':
                status_text = 'Дата оновлена 🟢'
            else:
                status_text = 'Помилка читання даних'
            status_messages.append(f"{order_number} : {date} : {status_text} : {status_file}")
        await update.message.reply_text(
            "\n".join(status_messages) or "Немає завдань для оновлення дати!")
    elif text == 'Очистити список ❌':
        await update.message.reply_text("Для очищення введіть пароль:")
    elif text == '42':
        save_orders({})
        await update.message.reply_text("Список очищений!")
    elif text == 'DTP' and update.message.from_user.id in admin_id:
        await update.message.reply_text(counter_check())
    elif order_number != 'Без номера' and date != 'Без дати':

        orders[order_number] = {
            "date": date,
            "status": "new",
            "file": status_file
        }

        save_orders(orders)

        await update.message.reply_text(
            f"Інформація прийнята {order_number} : {date}")
        print(f"Інформація прийнята {order_number} : {date}")
    elif text == 'Допомога 🧐':
        await update.message.reply_text('Інформація приймається у форматі:\n'
                                        'Номер замовлення і дата.\n'
                                        'Приклад: 12345 : 19.09\n'
                                        '\n'
                                        'Кнопки:\n'
                                        'Статуси замовлень ⚠️: показує статуси запитів з бази.\n'
                                        'Очистити список ❌: очищає базу для нових даних.\n'
                                        '\n'
                                        'Статуси:\n'
                                        '🔵 - Новий запит без оновлення дати.\n'
                                        '🔴️ - Немає технічної карти, замовлення в очікуванні.\n'
                                        '🟢 - Дату в технічній карті оновлено.\n'
                                        '✅ - Є файл PRINT.\n'
                                        '🅾️ - Файл відсутній.\n'
                                        '\n'
                                        'Деякі подробиці:\n'
                                        '1. Якщо файл для друку відсутній, повідомлення друкарю не надсилається.\n'
                                        '2. Перевірка наявності файлів здійснюється раз на 3 години за весь місяць і раз на 2 хвилини за сьогоднішню дату.\n'
                                        '3. Дані про замовлення, дата яких старша за два дні, видаляються.\n'
                                        '\n'
                                        'Якщо у вас є питання, ви можете задати їх тут:\n'
                                        'https://t.me/Gorea_Gregoire\n'
                                        '\n'
                                        'Але краще не відволікати 😉')

    else:
        await update.message.reply_text('Перефразуйте запит')


async def start(update: Update, context):
    keyboard = [
        [KeyboardButton('Статуси замовлень ⚠️')],
        [KeyboardButton('Очистити список ❌')],
        [KeyboardButton('Допомога 🧐')]
    ]
    if update.message.from_user.id in admin_id:
        keyboard.append([KeyboardButton('DTP')])
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text(
        "Привіт! Надішли мені текст замовлення, і я збережу його. Також можна використовувати кнопки нижче:",
        reply_markup=reply_markup)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот запущений...")
    app.run_polling()


if __name__ == "__main__":
    while True:
        try:
            update_orders_status()
            burnt()
            main()
        except Exception as f:
            print(f'reload bot...{f}')
            if str(f) == 'Event loop is closed':
                break
