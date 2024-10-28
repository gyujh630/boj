import sys

from collections import deque

def bfs(start, matrix, vst):
    queue = deque()
    queue.append(start)
    vst[start[0]][start[1]] = True  # 출발 지점
    matrix[start[0]][start[1]] = 0
    cnt = 1
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not vst[nx][ny] and matrix[nx][ny] == 1:
                    queue.append((nx, ny))
                    matrix[nx][ny] = 0
                    cnt += 1
                    vst[nx][ny] = True
    return cnt

N = int(sys.stdin.readline())

a = []
for _ in range(N):
    a.append(list(map(int, sys.stdin.readline().rstrip())))

result = []
while True:
    flag = False
    for i in range(N):
        for j in range(N):
            if a[i][j] == 1:
                flag = True
                visit = [[False] * N for _ in range(N)]
                result.append(bfs((i, j), a, visit))
                break
        if flag:
            break
    else:
        break

result.sort()
print(len(result))
for r in result:
    print(r)