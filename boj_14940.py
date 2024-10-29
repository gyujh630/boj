import sys
from collections import deque

def bfs(start, matrix, vst):
    queue = deque()
    queue.append(start)
    vst[start[0]][start[1]] = 0

    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if vst[nx][ny] == -1 and matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    vst[nx][ny] = vst[x][y] + 1
    return


N, M = map(int, sys.stdin.readline().split())
a = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

end = None
# 도착 지점 찾기
for i in range(N):
    for j in range(M):
        if a[i][j] == 2:
            end = (i, j)

visit = [[-1]*M for _ in range(N)]

bfs(end, a, visit)

for i in range(N):
    for j in range(M):
        if visit[i][j] == -1:
            if a[i][j] == 0:
                visit[i][j] = 0
        if j == M-1:
            print(visit[i][j])
        else:
            print(visit[i][j], end=' ')