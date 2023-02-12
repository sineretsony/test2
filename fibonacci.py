num_in = int(input("Введіть потрібну кількість чисел Фібоначчі: "))

# buffer zone
num_a = 0
num_b = 1
num_buf = 1
num_end = ", "

# cycle
while num_in > 0:
    print(f"{num_a}", end=f'{num_end}')
    num_a = num_b
    num_b = num_buf
    num_buf += num_a
    num_in -= 1
    if num_in == 1:
        num_end = ". "
