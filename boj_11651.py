#11651번: 좌표 정렬하기 2

import sys

n = int(sys.stdin.readline())
a = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    a.append([x,y])

a.sort(key = lambda x : (x[1], x[0]))

for i in a:
    print(i[0], i[1])