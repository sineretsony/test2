def calculate_ean13_checksum(barcode):
    odd_sum = sum(int(barcode[i]) for i in range(0, 12, 2))
    even_sum = sum(int(barcode[i]) for i in range(1, 12, 2))
    total_sum = odd_sum + even_sum * 3
    checksum = (10 - (total_sum % 10)) % 10
    return checksum

def generate_next_barcode(barcode):
    new_number = int(barcode[:-1]) + 1  # Увеличиваем последние 12 цифр
    new_number_str = str(new_number).zfill(12)  # Дополняем нулями до 12 цифр
    checksum = calculate_ean13_checksum(new_number_str)
    return new_number_str + str(checksum)

def save_barcodes_to_file(barcodes, filename="barcodes.txt"):
    with open(filename, "w") as file:
        for barcode in barcodes:
            file.write(barcode + "\n")
    print(f"Штрих-коды сохранены в файл {filename}")

def generate_barcodes(start_barcode, count):
    barcodes = [start_barcode]
    for _ in range(count - 1):  # Генерируем нужное количество кодов
        next_barcode = generate_next_barcode(barcodes[-1])
        barcodes.append(next_barcode)
    return barcodes

# Пример использования
barcode = "6291041501890"
count = 5000  # Количество штрих-кодов для генерации
barcodes = generate_barcodes(barcode, count)
save_barcodes_to_file(barcodes)

# Выводим результат
for i, code in enumerate(barcodes, 1):
    print(f"{i}: {code}")
