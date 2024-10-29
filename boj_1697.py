import sys
from collections import deque


def bfs(start, end, vst):
    queue = deque()
    queue.append(start)

    while queue:
        cur = queue.popleft()
        if cur == end:
            return vst[cur]
        for i in (cur-1, cur+1, cur*2):
            if 0 <= i < 100001 and not vst[i]:
                queue.append(i)
                vst[i] = vst[cur] + 1

    return



N, K = map(int, sys.stdin.readline().split())

visit = [0] * 100001
result = bfs(N, K, visit)
print(result)