# 팩토리얼 재귀함수로 구현
# BOJ 10872번

import sys
def factorial(n):
    if n == 0:
        return 1
    n = n * factorial(n-1)
    return n

n = int(sys.stdin.readline())
print(factorial(n))