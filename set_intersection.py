l1 = [1, 2, 2, 'three']
l2 = [9, 8, 2, 'three']
s1, s2 = set(l1), set(l2)
s3 = s1.intersection(s2)
q = 0
for i in s3:
    q += 1
print("Кількість спільних елементів: ", q)