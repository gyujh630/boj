# 1916번: 최소비용 구하기

import sys
import heapq

N = int(sys.stdin.readline())  # 도시의 개수 (<=1000)
M = int(sys.stdin.readline())  # 버스의 개수 (<=10만)
graph = [[] for _ in range(N+1)]
for m in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c)) # 도착지, 비용
start, end = map(int, sys.stdin.readline().split())


def dijkstra(graph, start):
    dists = [float('inf')] * (N + 1)
    dists[start] = 0
    queue = []
    heapq.heappush(queue, [dists[start], start])  # (거리, 노드)

    while queue:
        dist, node = heapq.heappop(queue)

        if dists[node] < dist:
            continue

        # 지금 꺼낸 node의 인접 탐색
        for next_node, next_dist in graph[node]:
            cur_dist = dist + next_dist  # 인접노드까지의 거리 계산
            if cur_dist < dists[next_node]:  # 갱신
                dists[next_node] = cur_dist
                heapq.heappush(queue, [cur_dist, next_node])
    return dists


dist_dp = dijkstra(graph, start)
print(dist_dp[end])