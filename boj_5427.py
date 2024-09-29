import sys
from collections import deque

def bfs_fire(board, fires, h, w):
    queue = deque()
    fire_time = [[-1] * w for _ in range(h)]

    for fire in fires:
        fx, fy = fire
        queue.append((fx, fy))
        fire_time[fx][fy] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] != '#' and fire_time[nx][ny] == -1:
                    fire_time[nx][ny] = fire_time[x][y] + 1
                    queue.append((nx, ny))
    return fire_time

def bfs_escape(board, sg_point, fire_time, h, w):
    queue = deque()
    escape_time = [[-1] * w for _ in range(h)]
    sx, sy = sg_point
    queue.append((sx, sy))
    escape_time[sx][sy] = 0

    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == '.' and escape_time[nx][ny] == -1:
                    if fire_time[nx][ny] == -1 or escape_time[x][y] + 1 < fire_time[nx][ny]:
                        escape_time[nx][ny] = escape_time[x][y] + 1
                        queue.append((nx, ny))
            else:
                return escape_time[x][y] + 1  # 탈출 성공

    return "IMPOSSIBLE"

t = int(sys.stdin.readline())
for _ in range(t):
    w, h = map(int, sys.stdin.readline().split())
    board = [list(sys.stdin.readline().strip()) for _ in range(h)]

    fires = []
    sg_point = None

    for i in range(h):
        for j in range(w):
            if board[i][j] == '*':
                fires.append((i, j))
            elif board[i][j] == '@':
                sg_point = (i, j)

    fire_time = bfs_fire(board, fires, h, w)
    result = bfs_escape(board, sg_point, fire_time, h, w)
    print(result)