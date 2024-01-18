#1012번: 유기농 배추

import sys
from collections import deque

def bfs(field, x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        cur = queue.popleft()
        dx, dy = [0, 1, -1, 0], [1, 0, 0, -1]
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 1:
                queue.append((nx, ny))
                field[nx][ny] = 0
    return 1

t = int(sys.stdin.readline().rstrip())
for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().split())
    field = [[0] * m for _ in range(n)]
    start_points = []
    count = 0

    for _ in range(k):
        i, j = map(int, sys.stdin.readline().split())
        field[i][j] = 1
        start_points.append((i, j))

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                count += bfs(field, i, j)
    print(count)


