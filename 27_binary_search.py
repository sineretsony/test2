sorted_list = [32, 38, 44, 45, 47, 53, 76, 99, 100, 108, 109,
               112, 127, 132, 140, 147, 158, 168, 170, 179]
key = 179


def search(n, k):
    """n = sorted list, k = search element"""
    left = 0
    right = len(n) - 1
    while left <= right:
        middle = (left + right) // 2
        if k == n[middle]:
            return middle
        elif k < n[middle]:
            right = middle - 1
        elif k > n[middle]:
            left = middle + 1
    return None


print(search(sorted_list, key))
