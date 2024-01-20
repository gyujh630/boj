#1780번: 종이의 개수

import sys

def count_picture(matrix, count):
    size = len(matrix)
    flag = 0
    first = matrix[0][0]
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != first:
                flag = 1
                break
    if flag == 1:
        new_size = size // 3
        for i in range(3):
            row_start = i*new_size
            row_end = row_start + new_size
            for j in range(3):
                column_start = j*new_size
                column_end = column_start + new_size
                new_matrix = [row[column_start:column_end] for row in matrix[row_start:row_end]]
                count_picture(new_matrix, count)
    else:
        count[matrix[0][0]] += 1
        return

n = int(sys.stdin.readline().rstrip())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
count = [0, 0, 0]

count_picture(matrix, count)
print(count[-1])
print(count[0])
print(count[1])