import keyboard


# код для порядковых чисел

def insert_number():
    global current_number
    current_number += 1
    number_str = f"{current_number:03d}"

    keyboard.write(number_str)


current_number = 1

keyboard.add_hotkey('tab', insert_number)

keyboard.wait()