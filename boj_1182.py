#1182번: 부분수열의 합

import sys

def find(pointer, total):
    global answer
    if pointer >= n:
        return
    find(pointer + 1, total) # 토탈에 현재 값이 반영되지 않음
    total += a[pointer]
    find(pointer + 1, total)  # 토탈에 현재 값 반영
    if total == s:
        answer += 1

n, s = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
answer = 0

find(0, 0)
print(answer)