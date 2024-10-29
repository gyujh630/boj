import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
q = deque()
for n in range(N):
    q.append(n+1)

result = []
for i in range(N):
    for j in range(K-1):
        q.append(q.popleft())
    result.append(q.popleft())

formatted_str = "<" + ", ".join(map(str, result)) + ">"
print(formatted_str)