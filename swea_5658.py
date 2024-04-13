# 삼성 SW 역량테스트 문제
# 5658번: 보물상자 비밀번호

from collections import deque


def rotate(string):
    tmp = string.pop()
    string.appendleft(tmp)
    return string


a_dic = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def make_decimal(string):
    global a
    new_dec = 0
    for i in range(len(string)):
        s = string[len(string) - 1 - i]
        if s.isalpha():
            new_dec += a_dic[s] * 16 ** i
        else:
            new_dec += int(s) * 16 ** i
    return new_dec


T = int(input())
for t in range(T):
    n, k = map(int, input().split())  # N은 4의 배수, 8 <= N <= 28
    s = input()
    s = deque(s)
    answer_set = []

    # 생성 가능한 수 구하기
    for m in range(0, n, n // 4):
        answer_set.append(list(s)[m:n // 4 + m])
    for j in range(n // 4 - 1):
        s = rotate(s)
        for x in range(0, n, n // 4):
            ele = list(s)[x:n // 4 + x]
            if ele not in answer_set:
                answer_set.append(list(s)[x:n // 4 + x])

    ans_list = []
    for ans in answer_set:
        s = ''
        for a in ans:
            s += a
        ans_list.append(make_decimal(s))
    ans_list.sort(reverse=True)
    print(f'#{t+1} {ans_list[k - 1]}')
