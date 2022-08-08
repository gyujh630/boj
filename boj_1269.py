#1269번: 대칭 차집합

import sys
n, m = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().strip().split()))
b = set(map(int, sys.stdin.readline().strip().split()))

print(len(a-b)+len(b-a))