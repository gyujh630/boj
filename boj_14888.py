# 삼성 역량테스트 기출
# 백준 14888번: 연산자 끼워넣기

import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
operator_index = list(map(int, sys.stdin.readline().split()))

# 덧셈, 뺄셈, 곱셈, 나눗셈 개수

dic = {0: 0, 1: 0, 2: 0, 3: 0}  # 더하기, 빼기, 곱하기, 나누기
for i in range(len(operator_index)):
    dic[i] = operator_index[i]

answer = []


def calculate(a, b, operator):
    if operator == 0:
        return a + b
    elif operator == 1:
        return a - b
    elif operator == 2:
        return a * b
    elif operator == 3:
        if a < 0:
            a = -a
            return -(a//b)
        return a // b


def func(index, remain_dic, result):
    num = arr[index]
    global answer

    # 종료 조건: 이번 index가 n일때
    if index == n-1:
        answer.append(result)
        return

    # 반복
    for key in remain_dic:
        if remain_dic[key] == 0:
            continue
        else:
            remain_dic[key] -= 1
            func(index + 1, remain_dic, calculate(result, arr[index+1], key))
            remain_dic[key] += 1


func(0, dic, arr[0])
print(max(answer))
print(min(answer))