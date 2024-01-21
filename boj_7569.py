#7569번: 토마토

import sys
from collections import deque

def bfs():
    queue = deque()
    for riped_tomato in riped_tomatoes:
        queue.append(riped_tomato)

    dx, dy, dz = [1, 0, 0, -1], [0, -1, 1, 0], [-1, 1]

    while queue:
        z, x, y = queue.popleft()
        #앞뒤좌우 탐색
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and matrix[z][nx][ny] == 0:
                matrix[z][nx][ny] = matrix[z][x][y] + 1
                queue.append((z, nx, ny))
        #상하 탐색
        for j in range(2):
            nz = z + dz[j]
            if 0 <= nz < h and matrix[nz][x][y] == 0:
                matrix[nz][x][y] = matrix[z][x][y] + 1
                queue.append((nz, x, y))


# 입력부
m, n, h = map(int, sys.stdin.readline().split())
matrix = [[list(map(int, sys.stdin.readline().split())) for _ in range(n)] for _ in range(h)]

# 익어있는 토마토 넣어두기 (시작점)
riped_tomatoes = []
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 1:
                riped_tomatoes.append((z, x, y))

bfs()

max = 0
for z in range(h):
    for x in range(n):
        for y in range(m):
            if matrix[z][x][y] == 0:
                print(-1)
                exit()
            if matrix[z][x][y] > max:
                max = matrix[z][x][y]
print(max-1)