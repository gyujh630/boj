# 7576번: 토마토

import sys
from collections import deque

def bfs(map, riped_tomatoes):
    queue = deque()
    count = 0
    temp = 0
    answer = 0
    total_change = 0
    for riped_tomato in riped_tomatoes: # 시작점 여러개 큐에 넣기
        queue.append(riped_tomato)
        temp += 1
        total_change += 1
    dx, dy = [0, -1, 1, 0], [1, 0, 0, -1]

    j = 1
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if map[nx][ny] == 0:
                    queue.append((nx, ny))
                    map[nx][ny] = 1
                    count += 1
                    total_change += 1
        if j == temp:
            answer += 1
            temp = count
            count = 0
            j = 0
        j += 1
    return answer - 1, total_change

# 입력 부분
m, n = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start_list = []
wall_count = 0

# 시작점(이미 익어 있는 토마토들) 탐색
for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            start_list.append((i, j))

# 벽(-1) 수 탐색
for i in range(n):
    for j in range(m):
        if map[i][j] == -1:
            wall_count += 1

answer, total = bfs(map, start_list)

if total != n * m - wall_count: #불가 여부 판단
    print(-1)
else: print(answer)
