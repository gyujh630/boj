# 16987번: 계란으로 계란치기

import sys


def count(eggs):
    cnt = 0
    for i in eggs:
        if i[0] <= 0:
            cnt += 1
    return cnt


def func(index, cur_eggs):
    global answer
    if index == n:
        # 카운트 체크
        answer = max(answer, count(cur_eggs))
        return

    left_egg = cur_eggs[index]
    left_w = left_egg[1]

    # 현재 계란 깨졌다면 다음 계란 들기
    if left_egg[0] <= 0:
        func(index + 1, cur_eggs)
    else:
        is_all_broken = True
        for i in range(n):
            if i != index and cur_eggs[i][0] > 0:
                is_all_broken = False
                right_egg = cur_eggs[i]
                right_w = right_egg[1]

                # 계란 치기
                left_egg[0] = left_egg[0] - right_w
                right_egg[0] = right_egg[0] - left_w
                # 재귀 함수 호출
                func(index + 1, cur_eggs)
                # 복구
                left_egg[0] = left_egg[0] + right_w
                right_egg[0] = right_egg[0] + left_w

        if is_all_broken:
            answer = max(answer, count(cur_eggs))
            return


n = int(sys.stdin.readline().rstrip())
eggs = list(list(map(int, sys.stdin.readline().split())) for _ in range(n))

answer = 0
func(0, eggs)

print(answer)

