import sys
input = sys.stdin.readline

n = int(input())

dx = [1,0,-1,0]
dy = [0,-1,0,1]

check = [[0] * (101) for _ in range(101)]

for _  in range(n):
    x,y,d,g = map(int,input().split())

    move_list = [d]
    check[x][y] = 1

    for i in range(g):
        tmp = []
        for j in range(len(move_list)):
            tmp.append((move_list[-j-1]+1)%4)
        move_list.extend(tmp)

    for i in move_list:
        nx = x + dx[i]
        ny = y + dy[i]
        check[nx][ny] = 1 # 체크처리
        x,y = nx,ny # 방향을 현재 움직인 방향으로 갱신

answer = 0

for i in range(100):
    for j in range(100):
        if check[i][j] == 1 and check[i+1][j] == 1 and check[i][j+1] == 1 and check[i+1][j+1] == 1:
            answer += 1

print(answer)