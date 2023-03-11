matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def transpose(t):
    try:
        elements_list = sum(t, [])
    except TypeError:
        print("Помилка, у вас не вкладений цикл")
        return None

    width, height = len(t[0]), len(t)

    def map_index(n, k, m=1):
        if m == n + 1:
            return []
        else:
            x = [y for y in reversed(range(m, n * k + 1, n))]
            return x + map_index(n, k, m + 1)

    link_ind = map_index(width, height)

    def add_results(n):
        results, temp = [], []
        for i in n:
            temp.append(elements_list[i - 1])
            if len(temp) == len(t):
                results.append(temp)
                temp = []
        return results

    matrix_rotation = add_results(link_ind)
    return matrix_rotation


print(transpose(matrix))

# ------------------------------------------------------------------

matrix2 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]


def transpose2(n):
    result2 = []
    calc = 0
    temp2 = []
    while len(result2) != len(n[0]):
        for i in range(len(n) - 1, -1, -1):
            temp2.append(n[i][calc])
            if len(temp2) == len(n):
                result2.append(temp2)
                temp2 = []
        calc += 1
    return result2


print(transpose2(matrix2))
