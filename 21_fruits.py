fruits = ['apple', 'banana', 'cherry', 'date', 'ananas']


def receiving_strings():
    temp_list, calc = [], 0
    for i in fruits:
        if i.lower()[0] in ['a', 'e', 'i', 'o', 'u', 'y']:
            temp_list.append(i)
        else:
            calc += 1
    conv = temp_list
    return conv, calc


print(receiving_strings())
