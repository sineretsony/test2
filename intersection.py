a = input("Бажаєте запровадити свої списки так/нi?: ")

if a == "так":
    s1 = []
    while True:
        q1 = input("Значення для I списку або stop: ")
        if q1.count("s"):
            break
        s1.append(q1)
    s2 = []
    while True:
        q2 = input("Значення для II списку або stop: ")
        if q2.count("s"):
            break
        s2.append(q2)
else:
    s1 = [1, 2, 3, 4, 5, 'six']
    s2 = [4, 5, 6, "six", 7, 8]

s3 = []

for i in s1:
    for z in s2:
        if s3.count(z):
            continue
        if i == z:
            s3.append(i)

print(f"Перетин двох списків {s3}")
