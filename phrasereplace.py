# Definition of initial data
question = input("Бажаєте ввести свою фразу 'так/ні'\n"
          "За замовчуванням буде використано:\n"
          "'hello hill house horse': ")

if question == "так":
    phrase = input("Введіть фразу: ")
else:
    phrase = "hello hill house horse"

# Finding and replacing the symbol H
space1 = phrase.find(" ")
space2 = phrase.rfind(" ")
search1 = phrase.find("h", space1)
search2 = phrase.find("h", space2)
slice_im = phrase[search1:search2]
replacement1 = slice_im.replace("h", "H")
result = phrase.replace(slice_im, replacement1)

print(result)
