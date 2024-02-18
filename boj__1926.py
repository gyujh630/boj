#1926번: 그림

import sys
from collections import deque


def bfs(map, x, y):
    queue = deque()
    queue.append((x, y))
    map[x][y] = 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 0

    while queue:
        cur = queue.popleft()
        count += 1
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if map[nx][ny] == 1:
                    queue.append((nx, ny))
                    map[nx][ny] = 0
    return count


n, m = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
max = 0
count = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            count += 1
            temp = bfs(map, i, j)
            if temp > max:
                max = temp

print(count)
print(max)

