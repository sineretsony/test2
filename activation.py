import os
import json
import socket
import telebot

# Телеграм бот токен
BOT_TOKEN = '7542441575:AAHVDWuOWzviO9m_muTZg4xbob91Iv9wYDE'
CHAT_ID = '-1002376400934'  # ID чата, где бот будет отправлять сообщения
ACTIVATION_FILE = 'activation.json'

# Инициализация бота
bot = telebot.TeleBot(BOT_TOKEN)


def save_activation_file(code):
    """Сохранение файла активации с кодом."""
    with open(ACTIVATION_FILE, 'w') as f:
        json.dump({'activation_code': code}, f)

def load_activation_code():
    """Загрузка кода активации из файла."""
    if os.path.exists(ACTIVATION_FILE):
        with open(ACTIVATION_FILE, 'r') as f:
            data = json.load(f)
            return data.get('activation_code')
    return None

def delete_activation_file():
    """Удаление файла активации."""
    if os.path.exists(ACTIVATION_FILE):
        os.remove(ACTIVATION_FILE)

def get_pinned_message():
    """Получение закреплённого сообщения из чата."""
    chat = bot.get_chat(CHAT_ID)
    if chat.pinned_message:
        return chat.pinned_message.text
    return None

def validate_activation_code():
    """Проверка существующего кода активации с закреплённым сообщением."""
    code = load_activation_code()
    if code:
        pinned_message = get_pinned_message()
        if pinned_message and code in pinned_message:
            print("Активация подтверждена.")
            bot.send_message(CHAT_ID, "Активация подтверждена. Программа запущена")
            return True
        elif 'day x' in pinned_message:
            pass
        else:
            print("Код активации недействителен....")
            delete_activation_file()
            return False
    return False

def activate():
    """Запрос нового кода активации через терминал."""
    code = input("Введите код активации: ")
    if code:
        print("Код активации отправлен. Ожидайте подтверждение.")
        bot.send_message(CHAT_ID, f"Код активации: {code} от {socket.gethostname()}")

        # Проверяем закрепленное сообщение на наличие кода
        pinned_message = get_pinned_message()
        if pinned_message and code in pinned_message:
            print("Активация прошла успешно!")
            bot.send_message(CHAT_ID,"Активация прошла успешно")
            save_activation_file(code)
        else:
            print("Код активации недействителен.")
    else:
        print("Код не введён.")

if __name__ == "__main__":
    # Проверяем файл активации и сверяем код с закреплённым сообщением
    if not validate_activation_code():
        activate()
