import time


def read_numbers_from_file():
    file_name = "intermediate_data.txt"

    while True:
        with open(file_name, "r") as file:
            numbers = file.readlines()

        for number in numbers:
            print(number.strip())

        time.sleep(2)  # Задержка между чтениями
read_numbers_from_file()