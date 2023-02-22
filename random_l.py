
import random

random_num = [random.randint(1, 200) for i in range(10)]
print(random_num)

lon_ran = len(random_num) - 2

for i in range(1, lon_ran):
    buf1 = random_num[i]
    buf2 = random_num[i + 1]
    buf3 = random_num[i + 2]
    if buf1 < buf2 > buf3:
        print(buf2)
