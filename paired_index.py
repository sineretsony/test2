#----------------Рішення 1------------------
#У цьому випадку ігнорується число без пари

s1 = [1, 2, 3, 4, 5, 10, 56]
s2 = [4, 5, 6, 7, 8]
s3 = []

if len(s1) > len(s2):
    buf = s1
    s1 = s2
    s2 = buf

len_num = len(s1)

for i in range(0, len_num, 2):
    res_pl = s1[i] + s2[i]
    s3.append(res_pl)

print(s3)
#----------------Рішення 2------------------
#У цьому випадку, додаєтеся 0 до меншого списку

s1 = [1, 2, 3, 4, 5, 10, 56]
s2 = [4, 5, 6, 7, 8]
s3 = []

if len(s1) < len(s2):
    buf = s1
    s1 = s2
    s2 = buf

while len(s1) > len(s2):
    s2.append(0)

len_num = len(s1)

for i in range(0, len_num, 2):
    res_pl = s1[i] + s2[i]
    s3.append(res_pl)

print(s3)
