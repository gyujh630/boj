import sys
from collections import deque


def dfs(start, cur):
    global count
    if visited[cur]:
        if S[cur] in select:
            count = len(select)
            return
    else:
        dfs(start, S[cur])


# T = int(sys.stdin.readline())
# for _ in range(T):
N = int(sys.stdin.readline())
S = [0] + list(map(int, sys.stdin.readline().split()))
visited = [False] * (N+1)
count = 0
for s in S:
    if not visited[s]:
        select = []
        dfs(s, s)

print(S)


