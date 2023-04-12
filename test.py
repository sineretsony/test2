# Исходная дата
date = '10.04.2124'

# Ключ шифрования
key = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Cras tempor ' \
      'at ex in pharetra. Etiam a elit at ex pharetra semper.'


# Функция для шифрования
def caesar(n):
    temp = ""
    slice_1 = 0
    slice_2 = 9
    count = 0
    for i in n:
        count += 1
        if count == 3 or count == 7:
            slice_1 += 9
            slice_2 += 9
        temp += chr((ord(i) + (slice_1 + slice_2)) % 256)
    return temp


z = caesar(date)
print(z)


def caesar_decrypt(s):
    slice_1 = 0
    slice_2 = 9
    result = ""
    count = 0
    for i in s:
        count += 1
        if count == 3 or count == 7:
            slice_1 += 9
            slice_2 += 9
        result += chr((ord(i) - (slice_1 + slice_2)) % 256)
    return result


print(caesar_decrypt(z))


