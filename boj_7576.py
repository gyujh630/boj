# 7576번: 토마토

import sys
from collections import deque


def bfs(map, riped_tomatoes, visited):
    queue = deque()
    count = 0
    temp = 0
    answer = 0
    total_change = 0
    for riped_tomato in riped_tomatoes:
        queue.append(riped_tomato)
        temp += 1
        total_change += 1
        visited[riped_tomato[0]][riped_tomato[1]] = True
    dx, dy = [0, -1, 1, 0], [1, 0, 0, -1]

    # temp = 2, count = 0 인 상태
    j = 1
    while queue:
        cur = queue.popleft()
        for i in range(4):
            nx, ny = cur[0] + dx[i], cur[1] + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and map[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
                    map[nx][ny] = 1
                    count += 1
                    total_change += 1
        # for k in range(n):
        #     print(map[k])
        # print(j, "번째 큐 결과")
        if j == temp:
            # print("count:", count, "이전 temp:", temp)
            # print("사이클 종료", j, "번째 사이클")
            answer += 1
            temp = count
            count = 0
            j = 0
        #     print("바뀐 temp:", temp)
        # print(" ")
        # print("answer:", answer)
        # print('--------------------')
        j += 1
    return answer - 1, total_change


m, n = map(int, sys.stdin.readline().split())
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
start_list = []
wall_count = 0

for i in range(n):
    for j in range(m):
        if map[i][j] == 1:
            start_list.append((i, j))

for i in range(n):
    for j in range(m):
        if map[i][j] == -1:
            wall_count += 1
visited = [[False] * m for _ in range(n)]
answer, total = bfs(map, start_list, visited)

if total != n*m-wall_count:
    print(-1)
else: print(answer)
