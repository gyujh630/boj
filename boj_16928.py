import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

def bfs(mtrx, lio, sio):
    queue = deque()
    queue.append(1)
    while queue:
        cur = queue.popleft()
        if lio[cur] > 0:
            nxt = lio[cur]
            if mtrx[nxt] == 0 or (mtrx[nxt] != 0 and mtrx[nxt] > mtrx[cur]):
                mtrx[nxt] = mtrx[cur]
                queue.append(nxt)
        elif sio[cur] > 0:
            nxt = sio[cur]
            if mtrx[nxt] == 0 or (mtrx[nxt] != 0 and mtrx[nxt] > mtrx[cur]):
                mtrx[nxt] = mtrx[cur]
                queue.append(nxt)
        else:
            for i in range(6):
                nxt = cur + (6-i)
                if 1 <= nxt <= 100:
                    if mtrx[nxt] == 0 or (mtrx[nxt] != 0 and mtrx[nxt] > mtrx[cur] + 1):
                        mtrx[nxt] = mtrx[cur] + 1
                        queue.append(nxt)
    return mtrx[100]

ladders = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))
snakes = list(list(map(int, sys.stdin.readline().split())) for _ in range(M))

ladder_io = [0] * 101
snakes_io = [0] * 101
for l in ladders:
    ladder_io[l[0]] = l[1]
for s in snakes:
    snakes_io[s[0]] = s[1]

matrix = [0] * 101
print(bfs(matrix, ladder_io, snakes_io))