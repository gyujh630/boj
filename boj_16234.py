# 16234번: 인구 이동
# 삼성 SW 역량테스트 기출

# 조건 1: 상하좌우 인접 칸의 인구 차이 L 이상 R 이하일 때 국경선 열림
# 1일 단위로 while 시뮬레이션 돌려서 더이상 안 될때 멈추기
# 모든 칸이 서로 차이가 없어야 멈추는 건데

import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

def bfs(start, un, vst, a):
    queue = deque()
    queue.append(start)
    un.append(start)
    vst[start[0]][start[1]] = True

    dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not vst[nx][ny]:
                    if l <= abs(a[x][y] - a[nx][ny]) <= r:
                        queue.append((nx, ny))
                        vst[nx][ny] = True
                        un.append((nx, ny))

    return un

day = 0

while True:
    visit = [[False] * n for _ in range(n)] # visit 초기화
    united = []
    for i in range(len(visit)):
        for j in range(len(visit)):
            if not visit[i][j]:
                un_group = bfs((i, j), [], visit, A)
                if len(un_group) > 1:
                    united.append(un_group)
    if len(united) == 0:
        break

    # 인구 이동
    for uni in united:
        # 각 연합을 순회
        sum = 0
        for u in uni: # 하나의 연합 안의 국가들을 돌면서
            sum += A[u[0]][u[1]]
        res = sum // len(uni)
        for u in uni:
            A[u[0]][u[1]] = res
    day += 1

print(day)