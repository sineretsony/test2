# buffer zone

num_imp = 0
num_qua = 0
num_sum = 0
num_ave = 0
num_max = 0
num_min = 0
nu_pair = 0
num_unp = 0

# cycle
while True:
    num_imp = int(input(": "))
    if num_imp == 0:
        break
    num_qua += 1
    num_sum += num_imp
    if num_min == 0:
        num_min = num_imp
    elif num_min == 0:
        if num_imp < num_min:
            num_min = num_imp
    if num_max == 0:
        num_max = num_imp
    if num_imp > num_max:
        num_max = num_imp
    a = num_imp % 2
    if a == 0:
        nu_pair += 1
    elif a > 0:
        num_unp += 1

# result
num_ave = num_sum / num_qua
print(f"Кількість введених чисел: {num_qua}\n"
      f"Сума введених чисел: {num_sum}\n"
      "Середнє арифметичне:", round(num_ave), "\n"
      f"Мінімальне значення: {num_min}\n"
      f"Максимальне значення: {num_max}\n"
      f"Парних: {nu_pair}\n"
      f"Непарних: {num_unp}")
