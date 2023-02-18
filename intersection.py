a = input("Бажаєте запровадити свої списки Y/N?: ")

if a == "Y":
    s1 = []
    while True:
        buf = input("Значення для I списку (stop в кінці): ")
        if buf.count("s"):
            break
        s1.append(buf)
    s2 = []
    while True:
        q2 = input("Значення для II списку (stop в кінці): ")
        if q2.count("s"):
            break
        s2.append(q2)
else:
    s1 = [1, 2, 3, 4, 5, 'six']
    s2 = [4, 5, 6, "six", 7, 8]

s3 = []

for i in s1:
    if i in s2 and i not in s3:
        s3.append(i)

print(f"Перетин двох списків {s3}")

# Хотів знайти спосіб, щоб цифри не залишалися str після введення,
# але не придумав як це зробити, тому що якщо дописати int,
# і ввести рядок літерами, буде помилка
