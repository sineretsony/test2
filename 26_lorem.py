with open('lorem.txt', 'r') as f:
    text = f.read()


def inp_text(x):
    dir_l = x.lower().replace(",", " ").replace(".", " ").split()
    dict_list = {}
    for i in dir_l:
        n = dir_l.count(i)
        dict_list[i] = n
    return dict_list


def writ_text(y):
    with open('stats.txt', 'w') as z:
        for i in y:
            z.write(i + ": " + str(y[i]) + "\n")


text_in_file = inp_text(text)
writ_text(text_in_file)
