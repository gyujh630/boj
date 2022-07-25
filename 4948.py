"""
< 시간초과 코드 >

import sys

def cal(n):
    a = []
    for i in range(n + 1, 2*n + 1):
        a.append(i)
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1
            continue
        for j in range(2, int(a[i] ** 0.5) + 1):
            if a[i] % j == 0:
                count += 1
                break
    return len(a) - count

n = int(sys.stdin.readline())
while True:
    if n == 0:
        break
    print(cal(n))
    n = int(sys.stdin.readline())
"""


#<통과 코드>

import sys

def is_sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

all_num = list(range(2,123456*2+1))

sosu_num = []
for i in all_num:
    if is_sosu(i):
        sosu_num.append(i)

n = int(sys.stdin.readline())
while True:
    count = 0
    if n == 0:
        break
    for i in sosu_num:
        if n<i<=2*n:
            count += 1
    print(count)
    n = int(sys.stdin.readline())

"""
<빠른 코드> 이해못했음.

import sys
def prime_num():
    att = [False] + [True for _ in range(123456*2)]
    for i in range(2, int((123456*2)**0.5)+1):
        if att[i]:
            for j in range(i*2, 123456*2+1, i):
                att[j] = False
    return att

result = prime_num()

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break
    print(sum(result[n+1:(2*n)+1]))

"""