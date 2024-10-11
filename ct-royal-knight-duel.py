#  코드트리 왕실의 기사 대결

import sys
from collections import deque

L, N, Q = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(L)]
knights = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(Q)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]  # 북 동 남 서

kn_board = [[0]*L for _ in range(L)]
damage = {}

# 기사 위치판
for i in range(len(knights)):
    kn = knights[i]
    r = kn[0] - 1
    c = kn[1] - 1
    for h in range(kn[2]):
        for w in range(kn[3]):
            kn_board[r+h][c+w] = i+1
    damage[i+1] = 0

def get_knight_xy(idx):
    for i in range(len(kn_board)):
        for j in range(len(kn_board)):
            if kn_board[i][j] == idx:
                return [True, i, j]
    return [False, -1, -1]

def bfs(start, dir, vst):
    queue = deque()
    queue.append(start)
    vst[start[0]][start[1]] = True
    push_list = [(start[0], start[1])]
    push_knight_idx = []
    while queue:
        x, y = queue.popleft()
        ax, ay = x + dx[dir], y + dy[dir]
        if L <= ax or ax < 0 or L <= ay or ay < 0:  # 가려는 방향이 보드를 넘어가거나
            # print(x, y, '보드 넘어감')
            return [], []
        elif board[x + dx[dir]][y + dy[dir]] == 2:  # 벽이 발견될 경우 종료
            # print(x, y, '벽 발견')
            return [], []
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < L and 0 <= ny < L:
                if not visit[nx][ny]:
                    # 현재와 다른 숫자지만 방향이 dir일때 or 현재와 같은 숫자
                    if ((kn_board[x][y] != kn_board[nx][ny]) and i == dir and kn_board[nx][ny] != 0) or (kn_board[x][y] == kn_board[nx][ny]):
                        queue.append((nx, ny))
                        vst[nx][ny] = True
                        push_list.append((nx, ny))
                        push_knight_idx.append(kn_board[nx][ny])
    if dir == 0:
        push_list.sort(key=lambda x: x[0])
    elif dir == 1:
        push_list.sort(reverse=True, key=lambda x: x[1])
    elif dir == 2:
        push_list.sort(reverse=True, key=lambda x: x[0])
    elif dir == 3:
        push_list.sort(key=lambda x: x[1])

    return push_list, set(push_knight_idx)

def push_knights(plist, dir):
    for p in plist:
        x, y = p[0], p[1]
        kn_board[x+dx[dir]][y+dy[dir]] = kn_board[x][y]
        kn_board[x][y] = 0
    return

def remove_knight(idx):
    for i in range(L):
        for j in range(L):
            if kn_board[i][j] == idx:
                kn_board[i][j] = 0

def mine_attack(attacker, pidx):
    for i in range(L):
        for j in range(L):
            if kn_board[i][j] != attacker and kn_board[i][j] > 0 and board[i][j] == 1 and kn_board[i][j] in pidx:  # 공격자가 아니고, 함정이 자리에 있는 경우
                target = kn_board[i][j]
                knights[target - 1][4] -= board[i][j] # 보드에 있는 함정에 의해 체력 깎음
                damage[target] += 1
                if knights[target - 1][4] <= 0:
                    remove_knight(target)
                    damage[target] = 0


for command in commands:
    i = command[0]  # 기사 번호
    d = command[1]  # 방향

    isAlive, sx, sy = get_knight_xy(i)
    if not isAlive:
        continue  # 죽은 기사. pass

    visit = [[False]*L for _ in range(L)]
    pushes, push_idx,  = bfs((sx, sy), d, visit)  # 밀어야 하는 영역 찾기 + 밀 수 있는지 검사

    if len(pushes) != 0:
        push_knights(pushes, d)  # 밀기
        mine_attack(i, push_idx)  # 함정 반영

result = []
ans = 0
for i in range(L):
    for j in range(L):
        if kn_board[i][j] != 0:
            result.append(kn_board[i][j])
result = list(set(result))

for r in result:
    ans += damage[r]
print(ans)