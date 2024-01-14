# 1021번: 회전하는 큐

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
out_list = list(map(int, sys.stdin.readline().split()))
q = deque()
for i in range(n):
    q.append(i + 1)

count = 0
i = 0
while i < m:
    if out_list[i] == q[0]:
        q.popleft()
        i += 1
    else:
        mid_index = int(len(q) / 2)
        if q.index(out_list[i]) <= mid_index:
            temp = q.popleft()
            q.append(temp)
            count += 1
        else:
            temp = q.pop()
            q.appendleft(temp)
            count += 1
print(count)
