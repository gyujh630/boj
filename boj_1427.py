import sys

n = sys.stdin.readline().strip()
n = list(n)
n.sort(reverse=True)
print(''.join(n))
