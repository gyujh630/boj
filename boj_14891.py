# 삼성 SW 역량테스트 준비
# 백준 14891번: 톱니바퀴

# [12시, 1시반, 3시, 4시반, 6시, 7시반, 9시, 10시반] -> 항상 유지.
# 닿는 부분은 항상 똑같다 -> index 2와 6 부분
# 앞뒤 제거에 편리한 deque를 사용하는게 좋을 듯

from collections import deque

fst = deque(map(int, input()))
sec = deque(map(int, input()))
trd = deque(map(int, input()))
fth = deque(map(int, input()))
gears = [0, fst, sec, trd, fth]
k = int(input())
rotate_info = [list(map(int, input().split())) for _ in range(k)]


# 특정 기어를 한 칸 회전시키는 함수
def rotate_gear(g, d):
    if d == 1:  # 시계
        temp = g.pop()
        g.appendleft(temp)
    else:
        temp = g.popleft()
        g.append(temp)


# 시뮬레이션
for rot in rotate_info:
    my_gear = gears[rot[0]]  # 회전할 톱니바퀴
    rot_dir = rot[1]  # 1: 시계, -1: 반시계
    a = [False, False, False]

    if gears[1][2] != gears[2][6]:
        a[0] = True
    if gears[2][2] != gears[3][6]:
        a[1] = True
    if gears[3][2] != gears[4][6]:
        a[2] = True

    rotate_gear(my_gear, rot_dir)
    if rot[0] == 1:
        if a[0]:
            rotate_gear(gears[2], rot_dir * -1)
            if a[1]:
                rotate_gear(gears[3], rot_dir)
                if a[2]:
                    rotate_gear(gears[4], rot_dir * -1)
    elif rot[0] == 2:
        if a[0]:
            rotate_gear(gears[1], rot_dir * -1)
        if a[1]:
            rotate_gear(gears[3], rot_dir * -1)
            if a[2]:
                rotate_gear(gears[4], rot_dir)
    elif rot[0] == 3:
        if a[2]:
            rotate_gear(gears[4], rot_dir * -1)
        if a[1]:
            rotate_gear(gears[2], rot_dir * -1)
            if a[0]:
                rotate_gear(gears[1], rot_dir)
    else:
        if a[2]:
            rotate_gear(gears[3], rot_dir * -1)
            if a[1]:
                rotate_gear(gears[2], rot_dir)
                if a[0]:
                    rotate_gear(gears[1], rot_dir * -1)

print(gears[1][0] + gears[2][0]*2 + gears[3][0]*4 + gears[4][0]*8)

