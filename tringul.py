import requests

# URL ссылки на файл
url = 'https://fex.net/ru/s/n82ddev'

# Заголовки, которые могут потребоваться для запроса
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Отправляем GET-запрос для получения страницы
response = requests.get(url, headers=headers)

# Проверяем, что запрос успешен
if response.status_code == 200:
    with open('file.zip', 'wb') as f:
        f.write(response.content)
    print('Файл успешно скачан.')
else:
    print('Ошибка при скачивании файла:', response.status_code)
