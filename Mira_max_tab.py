import keyboard

number_list = ["APPLE & KIWI",
               "TONIC APPLE",
               "VANILLA & CREAM",
               "LOLLY-POP CANDY",
               "FRESH MORINGA",
               "PURE MELISSA",
               "RASPBERRY & LIME",
               "PINEAPPLE SMOOTHIE",
               "SMOOTHIE RED & BLUEBERRIES",
               "Mango Tango",
               "Blackberry Nights",
               "Peony Song",
               "ORANGE BLOSSOM",
               "Magic Lotus",
               "MANDARIN GREEN TEA",
               "Play With Ginger",
               "GINGER LIME & VANILLA",
               "MIMOSA & CARDAMOM",
               "VANILLA",
               "PEACH & APRICOT",
               "Passion Freesia",
               "ITALIAN CAPPUCCINO",
               "COFFEE",
               "CHOCOLATE"]

current_index = 0


def insert_number():
    global current_index
    if current_index < len(number_list):
        number_str = f"{number_list[current_index]}"
        keyboard.write(number_str)
        current_index += 1


keyboard.add_hotkey('tab', insert_number)

keyboard.wait()
