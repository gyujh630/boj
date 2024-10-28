
import sys
from collections import deque

def bfs(start, matrix, vst):
    queue = deque()
    queue.append(start)
    vst[start[0]][start[1]] = 0  # 출발 지점

    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if vst[nx][ny] == -1 and matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    vst[nx][ny] = vst[x][y] + 1

    return vst[N-1][M-1] + 1

N, M = map(int, sys.stdin.readline().split())

a = list(list(map(int, sys.stdin.readline().rstrip())) for _ in range(N))

visit = list([-1] * M for _ in range(N))
print(bfs((0,0), a, visit))