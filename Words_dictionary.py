line = ("One, two, three, one, two, five. Two, five.")
dir_l = line.lower().replace(",", " ").replace(".", " ").split()
dict_list = {}
word_i, calc_num = "", 0
for i in dir_l:
    n = dir_l.count(i)
    dict_list[i] = n
    if n > calc_num:
        word_i, calc_num = i, n
    elif n == calc_num and not word_i.count(i):
        word_i += ", " + i
print(dict_list, word_i)
