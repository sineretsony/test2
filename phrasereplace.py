# Definition of initial data
question = input("Бажаєте ввести свою фразу 'так/ні'\n"
                 "За замовчуванням буде використано:\n"
                 "'hello hill house horse': ")

if question == "так":
    phrase = input("Введіть фразу: ")
else:
    phrase = "hello hill house horse"

# Finding and replacing the symbol H
num_len = len(phrase)

if num_len > 1 and phrase.count("h"):
    search1 = phrase.find("h")
    search2 = phrase.rfind("h")
    ed = search1 + 1
    slice_im = phrase[ed:search2]
    replacement1 = slice_im.replace("h", "H")
    bas = 0
    on_slic = phrase[bas:ed]
    th_slic = phrase[search2:num_len]
    result = on_slic + replacement1 + th_slic
elif num_len == 1 and phrase.count("h"):
    result = phrase
else:
    result = "У вашому рядку немає літер h"

print(result)
