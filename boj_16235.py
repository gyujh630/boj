# 16235번: 나무 재테크
# 삼성 기출

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees_input = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]
trees = [[deque() * N for _ in range(N)] for _ in range(N)]

for tree in trees_input:
    x, y, z = tree
    trees[x-1][y-1].append(z)

ground = [[5] * N for _ in range(N)]
dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

for k in range(K):
    # 봄: 자신의 나이만큼 양분을 먹고 나이가 1 성장한다.
    # 나이가 어린 나무부터 양분을 먹는다
    # 땅에 양분이 부족해서 못 먹는 나무는 죽는다.

    die_trees = []
    for i in range(N):
        for j in range(N):
            live_trees = deque()
            dead_nutrient = 0
            for k in range(len(trees[i][j])):  # i,j 자리의 나무들 확인
                age = trees[i][j][k]
                if ground[i][j] - age >= 0:
                    ground[i][j] -= age
                    live_trees.append(age + 1)
                else:
                    dead_nutrient += age // 2
            trees[i][j] = live_trees
            ground[i][j] += dead_nutrient

    # 가을: 번식
    # 나이가 5의 배수인 나무들 확인
    for i in range(N):
        for j in range(N):
            for k in range(len(trees[i][j])):
                age = trees[i][j][k]
                if age > 0 and age % 5 == 0:
                    for l in range(8):
                        nx, ny = i + dx[l], j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            trees[nx][ny].appendleft(1)
    # 겨울: 양분 추가
    for i in range(N):
        for j in range(N):
            ground[i][j] += A[i][j]


count = 0
for i in range(N):
    for j in range(N):
        count += len(trees[i][j])

print(count)