import sys

N, M = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

for i in range(1, len(a)):
    a[i] += a[i-1]
a = [0] + a

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(a[j]-a[i-1])

