# 9663번: N-Queen

import sys


def is_available(select, col):
    current_row = len(select)
    for row in range(current_row):
        # 수직 체크 or 대각선 체크
        if select[row] == col or abs(select[row] - col) == current_row - row:
            return False
    return True


def func(select, current_row):
    global total
    if current_row == n:
        total += 1
        return

    for col in range(n):
        if is_available(select, col):
            select.append(col)
            func(select, current_row+1)
            select.pop()


n = int(sys.stdin.readline())

total = 0

func([], 0)
print(total)
