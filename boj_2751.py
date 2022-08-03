import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))
a = sorted(set(a))
for i in range(len(a)):
    print(a[i])