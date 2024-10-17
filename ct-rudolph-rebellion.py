import sys
from collections import deque

N, M, P, C, D = map(int, sys.stdin.readline().split())
rr, rc = map(int, sys.stdin.readline().split())
santa_positions = [list(map(int, sys.stdin.readline().split())) for _ in range(P)]
santa_dict = {}
score = [0 for _ in range(P)]
board = [[0]*N for _ in range(N)]
dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북 동 남 서

# 보드에 루돌프, 산타 넣기.. + 딕셔너리로 위치, 점수 관리
board[rr-1][rc-1] = -1
for sp in santa_positions:
    board[sp[1]-1][sp[2]-1] = sp[0]
    santa_dict[sp[0]] = (sp[1]-1, sp[2]-1)
rr -= 1
rc -= 1

def get_nearest_santa():
    global rr, rc
    dists = []
    for num in santa_dict:
        sr, sc = santa_dict[num][0], santa_dict[num][1]  # 산타 좌표
        dists.append(((rr - sr)**2 + (rc - sc)**2, sr, sc))
    dists.sort(key=lambda x: (x[0], -x[1], -x[2]))
    return dists[0][1], dists[0][2]

def crash(mover, st_idx, back_d):
    global C, D, score

    t1, t2 = santa_dict[st_idx]
    # 누가 박았든 항상 산타만 밀려남
    if mover == 'r':  # 루돌프 충돌
        for _ in range(C):  # C만큼 밀려나기
            nr, nc = t1 + back_d[0], t2 + back_d[1]
            score[st_idx-1] += 1
            if 0 <= nr < N and 0 <= nc < N:
                board[t1][t2] = 0
                t1, t2 = nr, nc
                santa_dict[st_idx] = (nr, nc) # 딕셔너리에 반영
                board[nr][nc] = st_idx
            else:
                board[t1][t2] = 0
                santa_dict.pop(st_idx)
                break
    elif mover == 's':  # 산타 충돌
        print('mover s')
        for _ in range(D-1):  # D만큼 밀려나기 (아직 이동 안했기 때문에 -1)
            nr, nc = t1 + back_d[0], t2 + back_d[1]
            score[st_idx-1] += 1
            if 0 <= nr < N and 0 <= nc < N:
                board[t1][t2] = 0
                t1, t2 = nr, nc
                santa_dict[st_idx] = (nr, nc) # 딕셔너리에 반영
                board[nr][nc] = st_idx
            else:
                santa_dict.pop(st_idx)
                board[t1][t2] = 0
                break
    return

def r_move(t1, t2):
    global rr, rc
    st_idx = board[t1][t2]
    board[rr][rc] = 0
    a = rr - t1
    b = rc - t2
    c, d = 0, 0
    if a < 0: # 아래로
        c += 1
    elif a > 0: # 밑으로
        c -= 1
    if b < 0: # 우측으로
        d += 1
    elif b > 0: # 좌측으로
        d -= 1
    #맵에 반영
    rr += c
    rc += d
    board[rr][rc] = -1
    if rr == t1 and rc == t2:  # 충돌
        print('루돌프 -> 산타 충돌')
        crash('r', st_idx, (c, d))

def bfs(idx, st, vst):
    global rr, rc, dx, dy  # 목표지점 (루돌프 위치)
    queue = deque()
    queue.append(st)
    vst[st[0]][st[1]] = 1

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if vst[nx][ny] == 0 and board[nx][ny] <= 0 and board[nx][ny] != idx:  # 산타가 아닌 곳만 가능. 방문 x
                    queue.append((nx, ny))
                    vst[nx][ny] = vst[x][y] + 1
    if vst[rr][rc] > 0:
        return [True, vst[rr][rc]] # 루돌프까지 거리
    else: return [False, -1]

def s_move():
    global rr, rc, dx, dy
    for key in range(1, P+1):  # 1번 산타부터 움직이기
        if key not in santa_dict:
            continue
        santa = santa_dict[key]
        sx, sy = santa[0], santa[1]
        dists_min = []
        for i in range(4):
            visit = [[0] * N for _ in range(N)]
            nx1, ny1 = sx + dx[i], sy + dy[i]
            if not (0<=nx1<N and 0<=ny1<N):
                continue
            elif board[nx1][ny1] >= 1:
                continue
            available, dist = bfs(key, (sx + dx[i], sy + dy[i]), visit)
            if available:
                dists_min.append((dist, i))
        if len(dists_min) > 0:
            print(dists_min)
            dists_min.sort(key=lambda x: x[0])  # 최소 거리
            print(dists_min)
            min_d = dists_min[0][1]  # 최소 거리를 가는 방향
            # 산타 이동
            nx, ny = sx + dx[min_d], sy + dy[min_d]

            # 이동하면 루돌프 충돌?
            if nx == rr and ny == rc:
                crash("s", key, (dx[(min_d+2)%4], dy[(min_d+2)%4]))
            else:
                santa_dict[key] = (nx, ny)
                # 맵에 반영
                board[sx][sy] = 0
                board[nx][ny] = key
        print('산타들 움직임.', key)
        for i in board:
            print(i)
        print()

for i in board:
    print(i)
print()

# 게임 부분
for m in range(2): # 턴(M)

    # 루돌프로부터 가장 가까운 산타 찾기. 산타 딕셔너리에 항상 산타가 업데이트 되어야 가능
    tr, tc = get_nearest_santa()

    # 타겟 산타로 루돌프가 움직임 + 충돌 + 연쇄 충돌
    print('루돌프 움직임')
    r_move(tr, tc)
    for i in board:
        print(i)

    # 루돌프로 산타들이 움직임 + 충돌 + 연쇄 충돌
    s_move()
    #
    # print('산타들 움직임.')
    # for i in board:
    #     print(i)
    # print()
