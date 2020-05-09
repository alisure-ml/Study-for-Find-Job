"""
ABCCED
3 4
ABCESFCSADEE
SEE
3 4
ABCESFCSADEE

ABCE
SFCS
ADEE
"""
import sys

path = sys.stdin.readline().strip()
rows, cols = list(map(int, sys.stdin.readline().strip().split()))
# matrix = [input().strip().split() for i in range(rows)]
matrix = list(sys.stdin.readline())
matrix = [matrix[i * cols:(i + 1) * cols] for i in range(rows)]


def find(visit, matrix, rows, cols, path, row, col):
    if len(path) == 0:
        return True
    visit[row][col] = 1
    if col - 1 >= 0 and visit[row][col - 1] == 0 and matrix[row][col - 1] == path[0]:
        return find(visit, matrix, rows, cols, path[1:], row, col - 1)
    elif col + 1 < cols and visit[row][col + 1] == 0 and matrix[row][col + 1] == path[0]:
        return find(visit, matrix, rows, cols, path[1:], row, col + 1)
    elif row - 1 >= 0 and visit[row - 1][col] == 0 and matrix[row - 1][col] == path[0]:
        return find(visit, matrix, rows, cols, path[1:], row - 1, col)
    elif row + 1 < rows and visit[row + 1][col] == 0 and matrix[row + 1][col] == path[0]:
        return find(visit, matrix, rows, cols, path[1:], row + 1, col)
    else:
        return False
    pass


flag = False
for i in range(rows):
    for j in range(cols):
        if matrix[i][j] == path[0]:
            visit = [[0] * cols for _i in range(rows)]
            flag = find(visit, matrix, rows, cols, path[1:], i, j)
            if flag:
                break
    if flag:
        break
print(flag)
