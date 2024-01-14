#5430번: AC

import sys
from collections import deque

t = int(sys.stdin.readline())
p = []

#테스트 반복
for _ in range(t):
    p = sys.stdin.readline() #ex: TDD
    n = int(sys.stdin.readline()) #배열에 들어있는 숫자 수
    a = sys.stdin.readline().rstrip()
    if a =='[]':
        q = deque()
    else:
        a = list(map(int, a.strip("[""]").split(",")))  # [1,2,3,4] 처리
        q = deque(a)

    #최소화된 p 만들기
    min_p = []
    r_count = 0
    for i in p:
        if i == 'R': r_count += 1
        elif i == 'D' and r_count % 2 == 0:
            min_p.append('D')
            r_count = 0
        elif i == 'D' and r_count % 2 == 1:
            min_p.append('R')
            min_p.append('D')
            r_count = 0
    if r_count % 2 == 1:
        min_p.append('R')

    # #최소화한 명령어 실행
    flag = False
    reverse_count = 0
    for i in p:
        if i == 'D':
            if len(q) < 1:
                print("error")
                flag = True
                break
            if reverse_count % 2 == 0:
                q.popleft()
            else: q.pop()
        else:
            reverse_count += 1

    if reverse_count % 2 == 1:
        q.reverse()

    if flag == False:
        print("[" + ",".join(map(str, q)) + "]")








