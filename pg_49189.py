# 최단거리 이동
#
from collections import deque


def bfs(start, d, grp):
    queue = deque()
    queue.append(start)
    d[start] = 0

    while queue:
        cur = queue.popleft()
        for v in grp[cur]:
            if d[v] == -1:
                queue.append(v)
                d[v] = d[cur] + 1
    return


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]

    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    dist = [-1 for _ in range(n + 1)]
    bfs(1, dist, graph)

    for d in dist:
        if d == max(dist):
            answer += 1
    return answer