year = int(input("Введіть рік у форматі РРРР: "))

y1 = year // 100
y11 = year % 100

if y11 > 0:
    yy = y1 + 1
    print(f"Рік  відноситься до {yy} ст.")
elif y11 == 0:
    print(f"Этот год {year} відноситься до {y1} ст.")

