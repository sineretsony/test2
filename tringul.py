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

barcode = "6291041501890"
next_barcode = generate_next_barcode(barcode)
print("Следующий штрих-код:", next_barcode)
