import requests
import os
from urllib.parse import urlparse, parse_qs

# Список ссылок на файлы
urls = [
    "https://drive.google.com/file/d/1iZJYFT6PUkAvEIs6hb9xYQfvvUx7qWb5/view?usp=sharing",
    "https://drive.google.com/file/d/1XO5s6xxNd-gIwW1MlqE5wIsGy2gGq4ds/view?usp=sharing",
    "https://drive.google.com/file/d/1Vwhej47ox4zfow1up7TSK1Xw_2syH9rD/view?usp=drive_link"
]

# Путь к корневой папке на рабочем столе
root_folder = os.path.join(os.path.expanduser("~"), "Desktop", "files")

# Создаем корневую папку, если она не существует
os.makedirs(root_folder, exist_ok=True)


# Функция для загрузки файла по ссылке
def download_file(url):
    # Извлекаем идентификатор файла из ссылки
    file_id = url.split('/')[-2]
    # Загружаем файл
    response = requests.get(f"https://drive.google.com/uc?id={file_id}")
    # Получаем имя файла из заголовка ответа
    filename = response.headers['Content-Disposition'].split('filename=')[
        1].strip('"')
    # Путь к файлу
    file_path = os.path.join(root_folder,
                             filename.encode('latin1').decode('utf-8'))
    # Записываем файл
    with open(file_path, 'wb') as f:
        f.write(response.content)


# Загружаем каждый файл
for url in urls:
    download_file(url)
