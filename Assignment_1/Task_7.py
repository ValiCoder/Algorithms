# Task 7: Print the square that consists of NxN cells filled with numbers from 1 to N*N in a spiral mode (see examples).
# Note. Use recursion for solving this problem.


def spiralka(matrix, row_first, row_last, col_first, col_last, current_num):
    if row_first > row_last or col_first > col_last:
        return

    for i in range(col_first, col_last+1):
        matrix[row_first][i] = f"{current_num:2d}"
        current_num += 1

    for i in range(row_first+1, row_last+1):
        matrix[i][col_last] = f"{current_num:2d}"
        current_num += 1

    if row_first != row_last:
        for i in range(col_last-1, col_first-1, -1):
            matrix[row_last][i] = f"{current_num:2d}"
            current_num += 1

    if col_first != col_last:
        for i in range(row_last-1, row_first, -1):
            matrix[i][col_first] = f"{current_num:2d}"
            current_num += 1

    spiralka(matrix, row_first+1, row_last-1, col_first+1, col_last-1, current_num)

def print_matrix(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]
    spiralka(matrix, 0, n-1, 0, n-1, 1)
    for row in matrix:
        print(' '.join(map(str, row)))

n = int(input("Print the upper limit: "))
print_matrix(n)