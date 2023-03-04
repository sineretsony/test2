from itertools import permutations as perm

date_str = "abc"


def perm_str(s):
    for i in perm(date_str):
        yield "".join(i)


var = perm_str(date_str)

print(list(var))


