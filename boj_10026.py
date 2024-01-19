# 10026번: 적록색약

import sys
import copy
from collections import deque


def bfs(matrix, visited, x, y, color):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if matrix[nx][ny] == color and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return 1


n = int(sys.stdin.readline().rstrip())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
ab_matrix = copy.deepcopy(matrix)

for i in range(n):
    for j in range(n):
        if ab_matrix[i][j] == 'G':
            ab_matrix[i][j] = 'R'

normal_count = 0
abnormal_count = 0

visited = [[False] * n for _ in range(n)]
ab_visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G' or matrix[i][j] == 'B':
            if visited[i][j]:
                continue
            normal_count += bfs(matrix, visited, i, j, matrix[i][j])

for i in range(n):
    for j in range(n):
          if ab_matrix[i][j] == 'R' or ab_matrix[i][j] == 'B':
            if ab_visited[i][j]:
                continue
            abnormal_count += bfs(ab_matrix, ab_visited, i, j, ab_matrix[i][j])

print(normal_count, abnormal_count)
