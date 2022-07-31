import sys

def is_sosu(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

all_num = list(range(2, 10000))
sosu_num = []
for i in all_num:
    if is_sosu(i):
        sosu_num.append(i)

def comb(n):
    a = n//2
    b = n//2
    for i in range(int(n//2)+1):
        if a in sosu_num and b in sosu_num:
            print(a, b)
            break
        a -= 1
        b += 1

t = int(sys.stdin.readline())
for i in range(t):
    n = int(sys.stdin.readline())
    comb(n)
