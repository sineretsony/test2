import random

start = [random.randint(1, 200) for i in range(10)]

print(start)


def bubble_sort(n):
    swapped = True
    end = len(n) - 1
    while swapped:
        swapped = False
        for i in range(end):
            if n[i] > n[i + 1]:
                n[i], n[i + 1] = n[i + 1], n[i]
                swapped = True
        end -= 1


bubble_sort(start)

print(start)

#--------------------------------------------------------------------------

start2 = [random.randint(1, 200) for x in range(10)]

print(start2)


def bubble_sort(n):
    swapped = True
    end = len(n)-1
    while swapped:
        swapped = False
        for x in range(end):
            if n[x] > n[x+1]:
                n.insert(x, n[x+1])
                n.pop(x+2)
                swapped = True
        end -= 1
    return n


print(bubble_sort(start2))
