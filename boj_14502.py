import sys
from itertools import combinations
from collections import deque

def build_wall(comb):
    for index in comb:
        x, y = index[0], index[1]
        map[x][y] = 1 #벽세우기
    return

def destroy_wall(comb):
    for index in comb:
        x, y = index[0], index[1]
        map[x][y] = 0  # 벽부수기
    return

def calculate():
    visited = [[False] * len(map[0]) for _ in range(len(map))]
    new_map = [arr[:] for arr in map]  # map 복사
    zero_count = 0

    for virus in virus_list:
        dfs(new_map, virus[0], virus[1], visited)

    for row in new_map:
        zero_count += row.count(0)
    return zero_count

def dfs(map, x, y, visited):
    visited[x][y] = True
    queue = deque()
    queue.append([x,y])

    while(queue):
        v = queue.popleft()
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        for i in range(4):
            if 0 <= v[0] + dx[i] < n and 0 <= v[1] + dy[i] < m:
                nx, ny = v[0] + dx[i], v[1] + dy[i]
                if map[nx][ny] == 0 and [nx, ny] not in visited:
                    queue.append([nx, ny])
                    visited[nx][ny] = True
                    map[nx][ny] = 2

n,m = map(int, sys.stdin.readline().split(" "))
map = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

coords = [(x, y) for x in range(n) for y in range(m) if map[x][y] == 0]
combinations_list = list(combinations(coords, 3))

#2가 포함된 인덱스 미리 찾아놓기
virus_list = []
for i in range(n):
    for j in range(m):
        if map[i][j] == 2:
            virus_list.append((i,j))
max = 0

for comb in combinations_list:
    build_wall(comb)
    temp = calculate()
    if(temp>max):
        max = temp
    destroy_wall(comb)

print(max)
