# 2206번: 벽 부수고 이동하기

import sys
from collections import deque

def bfs(matrix, visited):
    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0][0] = 1
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if matrix[nx][ny] == '1':
                    if z == 0:
                        queue.append((nx, ny, 1))
                        visited[nx][ny][1] = visited[x][y][0] + 1
                else:
                    if visited[nx][ny][z] == 0:
                        queue.append((nx, ny, z))
                        visited[nx][ny][z] = visited[x][y][z] + 1
    return -1


n, m = map(int, sys.stdin.readline().split())
matrix = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

print(bfs(matrix, visited))
