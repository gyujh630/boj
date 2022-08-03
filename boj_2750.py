import sys

n = int(sys.stdin.readline())
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))
print('\n'.join(map(str, sorted(num))))