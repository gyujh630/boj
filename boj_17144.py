# 17144번: 미세먼지 안녕!
# 삼성 기출

import sys

r, c, t = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]

# 공기청정기, 미세먼지 위치 찾기
cleaner = []
for i in range(r):
    for j in range(c):
        if a[i][j] == -1:
            cleaner.append((i, j))

dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

# Simulation
for _ in range(t):
    b = [[0] * c for _ in range(r)]  # 가중치 배열
    dust = []
    # 미세 먼지 찾기
    for i in range(r):
        for j in range(c):
            if a[i][j] > 0:
                dust.append((i, j))

    # 칸 별 확산량 체크
    for d in dust:
        x, y = d[0], d[1]  # 현재 미세 먼지 칸
        amount = a[x][y]
        count = 0

        # 인접 칸 검증
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]  # 인접 칸이
            if 0 <= nx < r and 0 <= ny < c:  # 범위 안에 있고
                if a[nx][ny] != -1:  # 공기 청정기 아닌 경우
                    count += 1  # 확산 횟수 체크
                    b[nx][ny] += amount // 5  # 가중치 반영

        b[x][y] -= (amount // 5) * count  # 시작점 가중치 반영

    # 확산 적용
    for i in range(r):
        for j in range(c):
            a[i][j] += b[i][j]
    #
    # for j in a:
    #     print(j)
    # print()

    for i in range(r):
        i = r - 1 - i  # 6, 5, 4, ...
        if 0 < i < cleaner[0][0]:
            a[i][0] = a[i-1][0]  # 이동
    for i in range(r):
        if cleaner[1][0] < i < r - 1:
            a[i][0] = a[i + 1][0]  # 이동

    for j in range(0, c-1):
        a[0][j] = a[0][j + 1]  # 이동
        a[r-1][j] = a[r-1][j+1]

    for i in range(r):
        if 0 < i <= cleaner[0][0]:
            a[i-1][c - 1] = a[i][c - 1]

    for i in range(r):
        i = r - 1 - i # 6, 5, 4, ...
        if i > cleaner[1][0]:
            a[i][c - 1] = a[i-1][c - 1]

    for j in range(c-1):
        j = c - 1 - j
        a[cleaner[0][0]][j] = a[cleaner[0][0]][j-1]
        a[cleaner[1][0]][j] = a[cleaner[1][0]][j-1]
    a[cleaner[0][0]][1] = 0
    a[cleaner[1][0]][1] = 0
    # for j in a:
    #     print(j)
    # print()



result = 0
for i in range(r):
    for j in range(c):
        if a[i][j] != -1:
            result += a[i][j]

print(result)