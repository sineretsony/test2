year = int(input("Введіть рік у форматі РРРР: "))

year_di = year // 100
year_trig = year % 100

if year_trig > 0:
    year_align = year_di + 1
    print(f"Рік  відноситься до {year_align} ст.")
elif year_trig == 0:
    print(f"Этот год {year} відноситься до {year_di} ст.")

