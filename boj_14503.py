# 삼성역테
# 백준 14503번: 로봇 청소기


'''
로봇 청소기의 작동 방식

주변 4칸을 살핌
청소되지 않은 게 하나라도 있으면? -> 반시계 90도 방향회전 반복하며 청소되지 않은 칸 찾고 전진
'''

n, m = map(int, input().split())
r, c, d = map(int, input().split()) # 0,1,2,3 = 북동남서 -> 남서북동
cur = (r, c, d)

matrix = []
count = 0
front_map = [(-1, 0), (0, 1), (1, 0), (0, -1)]
back_map = [(1, 0), (0, -1), (-1, 0), (0, 1)]
for i in range(n):
    matrix.append(list(map(int, input().split())))


while True:
    # for i in range(n):
    #     print(matrix[i])
    # print()
    if matrix[cur[0]][cur[1]] == 0:
        matrix[cur[0]][cur[1]] = 2
        count += 1
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1] # 북동남서
    clean_flag = False
    for i in range(4):
        nx, ny = cur[0] + dx[i], cur[1] + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 0: # 청소 되지 않은 빈칸이 존재
                # i가 곧 가야 할 방향이다.
                # cur = (nx, ny, i) # 방향전환 및 전진
                clean_flag = True
                break
    if clean_flag:
        # 방향 전환 90도 반시계
        if cur[2] == 0:
            cur = (cur[0], cur[1], 3)
        else:
            cur = (cur[0], cur[1], cur[2] - 1)
        now_d = cur[2]
        front_x, front_y = cur[0] + front_map[now_d][0], cur[1] + front_map[now_d][1]
        if 0 > front_x >= n or 0 > front_y >= m or matrix[front_x][front_y] == 0:
            cur = (front_x, front_y, now_d)

    else:
        now_d = cur[2]
        back_x, back_y = cur[0] + back_map[now_d][0], cur[1] + back_map[now_d][1]

        if 0 > back_x >= n or 0 > back_y >= m or matrix[back_x][back_y] == 1:
            break
        else:
            cur = (back_x, back_y, now_d)

print(count)









