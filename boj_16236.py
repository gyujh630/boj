# 백준 16236번: 아기 상어

from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]

# 아기 상어 위치, 물고기 위치 파악하기
baby_shark = ()
for i in range(n):
    for j in range(n):
        if space[i][j] == 9:
            baby_shark = (i, j, 2)  # 아기상어 초기 세팅

fish_list = []
for i in range(n):
    for j in range(n):
        if 1 <= space[i][j] <= 6 and space[i][j] < baby_shark[2]:
            distance = abs(i - baby_shark[0]) + abs(j - baby_shark[1])
            fish_list.append((i, j, space[i][j], distance))


def bfs(x, y, shark_size):
    vst = [[0] * n for _ in range(n)]
    eats = []
    queue = deque()
    queue.append([x, y])
    vst[x][y] = 1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and vst[nx][ny] == 0:
                if space[nx][ny] <= shark_size:
                    queue.append((nx, ny))
                    vst[nx][ny] = vst[x][y] + 1
                    if space[nx][ny] != 0 and space[nx][ny] < shark_size:
                        eats.append((nx, ny, vst[nx][ny]-1))
    return sorted(eats, key=lambda z: (z[2], z[0], z[1]))  # 거리, x, y 순으로 오름차순


time = 0
size_checker = 0

while True:
    fish = bfs(baby_shark[0], baby_shark[1], baby_shark[2])
    # 종료 조건
    if not fish:
        break

    nx, ny, d = fish[0]
    time += d
    size_checker += 1

    # 먹은 물고기 수와 크기가 같다면 크기 1 증가
    if baby_shark[2] == size_checker:
        baby_shark = (baby_shark[0], baby_shark[1], baby_shark[2] + 1)
        size_checker = 0

    # 상어좌표를 먹은 물고기 좌표로 옮겨준다.
    space[baby_shark[0]][baby_shark[1]] = 0
    baby_shark = (nx, ny, baby_shark[2])

print(time)
