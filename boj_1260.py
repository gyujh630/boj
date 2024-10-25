import sys
from collections import deque

def bfs(start, grp, vst):
    arr = []
    queue = deque()
    queue.append(start)
    vst[start] = True
    arr.append(start)
    while queue:
        cur = queue.popleft()
        for i in range(len(grp[cur])):
            if not vst[grp[cur][i]]:
                queue.append(grp[cur][i])
                vst[grp[cur][i]] = True
                arr.append(grp[cur][i])
    return arr

def dfs(cur, selected, length, grp):
    dfs_result.append(cur)
    for i in range(1, len(graph)+1):  # 1, 2, 3, 4
        # cur 에서 갈 수 있는 곳들
        if i in grp[cur] and i not in selected:
            selected.append(i)
            dfs(i, selected, length, grp)


N, M, V = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for m in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 번호가 작은 것을 먼저 방문하기 위해 정렬
for i in range(1, N + 1):
    graph[i].sort()

visit = [False for _ in range(N+1)]
bfs_result = bfs(V, graph, visit)
dfs_result = []
dfs(V, [V], N, graph)

print(*dfs_result)
print(*bfs_result)