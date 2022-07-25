import sys
n = int(sys.stdin.readline())
b = []
for i in range(n):
    b.append(tuple(map(int, sys.stdin.readline().split())))

b = sorted(b)

for i in range(len(b)):
    print(b[i][0], b[i][1])