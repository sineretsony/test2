
l1 = [1, 2, 2, 'three']
l2 = [9, 8, 2, 'three']

s3 = set(l1).intersection, set(l2)
q = len([i for i in s3])

print("Кількість спільних елементів: ", q)
