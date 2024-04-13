# 삼성 SW 역량 테스트 준비
# 백준 14499번: 주사위 굴리기

n, m, x, y, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
command = list(map(int, input().split()))
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}  # 동서북남 좌표 이동 구현
dice = {'위': 0, '아래': 0, '동': 0, '서': 0, '남': 0, '북': 0}
cur = (x, y)


def east(dice_dic):
    # 동쪽으로 돌기
    # 위, 아래, 동, 서 4개가 바뀜
    top, est, bottom, wst = dice_dic['위'], dice_dic['동'], dice_dic['아래'], dice_dic['서']
    dice_dic['위'] = wst
    dice_dic['동'] = top
    dice_dic['아래'] = est
    dice_dic['서'] = bottom
    return dice_dic


def west(dice_dic):
    # 서쪽으로 돌기
    # 위, 아래, 동, 서 4개가 바뀜
    top, est, bottom, wst = dice_dic['위'], dice_dic['동'], dice_dic['아래'], dice_dic['서']
    dice_dic['위'] = est
    dice_dic['동'] = bottom
    dice_dic['아래'] = wst
    dice_dic['서'] = top
    return dice_dic


def north(dice_dic):
    # 북쪽으로 돌기
    # 위, 아래, 북, 남 4개가 바뀜
    top, nth, bottom, sth = dice_dic['위'], dice_dic['북'], dice_dic['아래'], dice_dic['남']
    dice_dic['위'] = sth
    dice_dic['북'] = top
    dice_dic['아래'] = nth
    dice_dic['남'] = bottom
    return dice_dic


def south(dice_dic):
    # 남쪽으로 돌기
    # 위, 아래, 북, 남 4개가 바뀜
    top, nth, bottom, sth = dice_dic['위'], dice_dic['북'], dice_dic['아래'], dice_dic['남']
    dice_dic['위'] = nth
    dice_dic['북'] = bottom
    dice_dic['아래'] = sth
    dice_dic['남'] = top
    return dice_dic


for cm in command:
    # cm -> 1 or 2 or 3 or 4 (방향)
    dx, dy = direction[cm]
    nx, ny = cur[0] + dx, cur[1] + dy
    if 0 <= nx < n and 0 <= ny < m:
        # 바깥으로 이동시키지 않는 경우만 해당
        cur = (nx, ny)  # 이동
        if cm == 1:  # 주사위 굴리기
            dice = east(dice)
        elif cm == 2:
            dice = west(dice)
        elif cm == 3:
            dice = north(dice)
        elif cm == 4:
            dice = south(dice)
        print(dice['위'])
        # 이동한 칸에 쓰여 있는 수가 0이면, 주사위 바닥 면에 쓰여 있는 수가 칸에 복사
        if matrix[nx][ny] == 0:
            matrix[nx][ny] = dice['아래']
        # 0이 아닌 경우엔 칸에 쓰여 있는 수가 주사위 바닥 면으로 복사, 칸에 쓰여 있는 수는 0이 된다.
        else:
            dice['아래'] = matrix[nx][ny]
            matrix[nx][ny] = 0


