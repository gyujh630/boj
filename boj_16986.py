# 16986번: 인싸들의 가위바위보

import sys


def func(count, i, left_p, right_p):
    if count[0][0] == k:
        return True
    if i == 20 or count[0][1] > n:
        return False
    # 지우가 참여하는 게임 지우 vs 경희 or 지우 vs 민호

    return


def select_winner(left, right):
    global c
    return c[left - 1][right - 1]


n, k = map(int, sys.stdin.readline().split())

c = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

kh_list = list(map(int, sys.stdin.readline().split()))
mh_list = list(map(int, sys.stdin.readline().split()))

count = [(0, 1), (0, 1), (0, 0)]  # 지우, 경희, 민호.. win count / 현재 몇번 참여
# 지우가 낼 수 있는 리스트.. [1, 1, 1]
# 시작은 항상 지우이다. 지우, 경희 -> 승자가 .. pop, append로 해결하고

func(count, 1, "j", "k");