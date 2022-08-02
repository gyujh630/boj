#2231번: 분해합

"""
import sys
n = int(sys.stdin.readline())

result = n

for i in range(1, n+1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])       #i를 자릿수마다 나누어 더해주는 부분
    if sum + i == n and i < result: #i가 생성자이고 최솟값이라면
        result = i                  #결과값에 할당

if result == n:                     #결과값이 처음과 똑같다면 (생성자가 없는 것임)
     print(0)
else: print(result)
"""

import sys
n = int(sys.stdin.readline())

                                   #추가코드
min = n - (len(str(n))*9)          #n의 생성자가 될 수 있는 최솟값
if min <= 0:                       #이 최솟값이 음수가 된 경우 1로 초기화
    min = 1

result = n

for i in range(min, n+1):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])       #i를 자릿수마다 나누어 더해주는 부분
    if sum + i == n and i < result: #i가 생성자이고 최솟값이라면
        result = i                  #결과값에 할당

if result == n:                     #결과값이 처음과 똑같다면 (생성자가 없는 것임)
     print(0)
else: print(result)