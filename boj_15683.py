# 삼성 SW 역량테스트
# 백준 15683번: 감시

from collections import deque
import copy


def search(start, tmp, direction):
    queue = deque()
    queue.append(start)
    d = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while queue:
        x, y = queue.popleft()
        nx, ny = x + d[direction][0], y + d[direction][1]
        if 0 <= nx < n and 0 <= ny < m and tmp[nx][ny] != 6:
            queue.append((nx, ny))
            tmp[nx][ny] = '#'


def backtracking(idx, ddc):
    global mini
    if idx == len(cctv_list):  # 종료
        tmp = copy.deepcopy(matrix)
        for i in range(len(ddc)):
            for j in range(len(ddc[i])):
                search((cctv_list[i][1], cctv_list[i][2]), tmp, ddc[i][j])
        count = 0
        for i in range(n):
            count += tmp[i].count(0)
        mini = min(mini, count)
        return

    for m in mode[cctv_list[idx][0]]:
        ddc.append(m)
        backtracking(idx+1, ddc)
        ddc.pop()


mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cctv_idx = {1, 2, 3, 4, 5}
cctv_list = []
for i in range(n):
    for j in range(m):
        if matrix[i][j] in cctv_idx:
            cctv_list.append((matrix[i][j], i, j))
mini = int(1e9)


backtracking(0, [])
print(mini)
