
l1 = [1, 2, 2, 'three']
l2 = [9, 8, 2, 'three']

s3 = set(l1).intersection, set(l2)
q = 0

for i in s3:
    q += 1

print("Кількість спільних елементів: ", q)