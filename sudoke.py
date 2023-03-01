m = [1, 7, 9, 3, 2, 8, 5, 6, 4,
     4, 3, 8, 6, 5, 9, 1, 7, 2,
     2, 5, 6, 7, 1, 4, 3, 8, 9,
     3, 2, 4, 8, 9, 1, 7, 5, 6,
     7, 9, 5, 4, 3, 6, 2, 1, 8,
     8, 6, 1, 2, 7, 5, 9, 4, 3,
     5, 8, 2, 1, 4, 3, 6, 9, 7,
     9, 4, 7, 5, 6, 2, 8, 3, 1,
     6, 1, 3, 9, 8, 7, 4, 2, 5]

one, nine = 1, 9


def get_row(n):
    row = [m[i:i + 9] for i in range(0, len(m), 9)]
    row_results = row[n - 1]
    return row_results


def get_column(n):
    column = [m[x::9] for x in range(len(m))]
    col_results = column[n - 1]
    return col_results


def get_squares(n):
    squares = []
    a = 0
    while a <= 60:
        squares.append(m[a:a + 3] + m[a + 9:a + 12] + m[a + 18:a + 21])
        a += 3
        if a == 9 or a == 33:
            a += 18
    squ_results = squares[n - 1]
    return squ_results


print(f"Рядок {one}", get_row(one),
      f"\nРядок {nine}", get_row(nine))
print(f"Колонка {one}", get_column(one),
      f"\nКолонка {nine}", get_column(nine))
print(f"Квадрат {one}", get_squares(one),
      f"\nКвадрат {nine}", get_squares(nine))
