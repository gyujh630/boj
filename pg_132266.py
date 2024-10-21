from collections import deque


def bfs(dest, grp, n):
    queue = deque()

    # 목적지에서 출발
    queue.append(dest)
    vst = [-1] * (n + 1)  # 방문체크 list
    vst[dest] = 0

    while queue:
        cur = queue.popleft()
        nexts = grp[cur]
        for next in nexts:
            if vst[next] == -1:  # 방문 안한 경우만
                queue.append(next)
                vst[next] = vst[cur] + 1  # 이전 거리에 + 1
    return vst


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for r in roads:
        graph[r[0]].append(r[1])
        graph[r[1]].append(r[0])

    visit = bfs(destination, graph, n)

    answer = []
    for src in sources:
        answer.append(visit[src])

    return answer