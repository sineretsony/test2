str_revers = "abcd sdgs"


def recur_fun(n):
    if len(n) == 0:
        return n
    else:
        return n[-1] + recur_fun(n[:-1])


def cyc_whi(n):
    results = ""
    index_str = -1
    while len(results) != len(n):
        results += (n[index_str])
        index_str -= 1
    return results


def cyc_for(n):
    temp = []
    for i in n:
        temp.insert(0, i)
    return "".join(temp)


print(recur_fun(str_revers))
print(cyc_whi(str_revers))
print(cyc_for(str_revers))
