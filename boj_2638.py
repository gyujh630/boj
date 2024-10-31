import sys
from collections import deque
'''

cycle
1. (0,0)은 항상 외부이다. (모눈종이 가장자리에 치즈가 없으므로)
2. (0,0)에서 bfs를 돌려서 외부를 1, 치즈들 + 치즈 내부는 0으로 표시하는 2차원 리스트 반환(A) -> 치즈 내부까지 치즈로 취급
3. A 배열에서, 치즈 자리에서부터 bfs
4. 돌리면서 체크하고 지울 건 지워준다.
'''

N, M = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def outer_bfs(start, matrix):
    visit = [[0]*M for _ in range(N)]
    cnt = 1
    queue = deque()
    queue.append(start)
    visit[0][0] = 1
    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if visit[nx][ny] == 0 and matrix[nx][ny] == 0:
                    visit[nx][ny] = 1
                    cnt += 1
                    queue.append((nx, ny))
    return cnt, visit

time = 0
while True:
    # (0,0)에서 bfs 수행
    count, outer_arr = outer_bfs((0,0), arr)
    if count == N*M:
        print(time)
        break
    for i in range(N):
        for j in range(M):
            if outer_arr[i][j] == 0:
                di, dj = [1, 0, 0, -1], [0, 1, -1, 0]
                check = 0
                for k in range(4):
                    ni, nj = i + di[k], j + dj[k]
                    if 0 <= ni < N and 0 <= nj < M:
                        if outer_arr[ni][nj] == 1:
                            check += 1
                if check >= 2:
                    arr[i][j] = 0
    time += 1

