#1992번: 쿼드트리

import sys

def quad_tree(matrix):
    size = len(matrix)
    start_point = matrix[0][0]
    flag = 0
    for i in range(size):
        for j in range(size):
            if matrix[i][j] != start_point:
                flag = 1
                break
    if flag == 1:
        new_matrices = []
        new_size = size // 2
        for k in range(2):  # k = 0,1
            row_start = k * new_size
            row_end = row_start + new_size
            for l in range(2):  # l = 0,1
                column_start = l * new_size
                column_end = column_start + new_size
                new_matrix = [row[column_start:column_end] for row in matrix[row_start:row_end]]
                new_matrices.append(new_matrix)
        return '(' + quad_tree(new_matrices[0]) + quad_tree(new_matrices[1]) + quad_tree(new_matrices[2]) + quad_tree(new_matrices[3]) + ')'
    return start_point


n = int(sys.stdin.readline())
matrix = []
for _ in range(n):
    matrix.append(list(sys.stdin.readline().rstrip()))


print(quad_tree(matrix))