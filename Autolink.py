import requests
from bs4 import BeautifulSoup

# Ввод URL
file_url = input("Введите ссылку на файл: ")

# URL для входа
login_url = 'https://ru.freepik.com/login'

# Данные для входа
payload = {
    'email': 'Mashod@gmail.com',
    'password': 'P@7wBgp!Fy@!4XR'
}

# Создание сессии
session = requests.Session()

# Логин
login_response = session.post(login_url, data=payload)

# Проверка успешности входа
if login_response.status_code == 200:
    print("Вход выполнен успешно.")

    # Получение страницы с файлом
    file_page_response = session.get(file_url)

    # Проверка успешности получения страницы
    if file_page_response.status_code == 200:
        print("Страница файла загружена успешно.")

        # Парсинг страницы
        soup = BeautifulSoup(file_page_response.content, 'html.parser')

        # Логирование HTML для анализа
        with open('page.html', 'w', encoding='utf-8') as f:
            f.write(soup.prettify())

        # Попытка найти ссылку на скачивание файла
        download_button = soup.find('a', {'class': 'btn btn-primary btn-user'})

        if download_button:
            download_link = download_button['href']
            print(f'Ссылка на скачивание: {download_link}')

            # Скачать файл
            file_response = session.get(download_link, stream=True)

            if file_response.status_code == 200:
                # Извлечение имени файла из URL
                file_name = download_link.split('/')[-1]

                # Сохранение файла
                with open(file_name, 'wb') as file:
                    for chunk in file_response.iter_content(chunk_size=8192):
                        file.write(chunk)
                print(f'Файл {file_name} успешно загружен.')
            else:
                print('Не удалось скачать файл.')
        else:
            print('Ссылка на скачивание не найдена.')
    else:
        print('Не удалось получить страницу файла.')
else:
    print('Не удалось войти на сайт. Проверьте данные для входа.')
