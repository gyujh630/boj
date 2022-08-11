import sys

n = int(sys.stdin.readline())
a = [0] * 10001 # 문제에서 주어진 범위인 10000개만큼의 0으로 이루어진 배열을 만들어 놓는다

for i in range(n):
    new = int(sys.stdin.readline())
    a[new] += 1

for i in range(len(a)):
    for j in range(a[i]):
        print(i)
