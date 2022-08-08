#1010번: 다리 놓기

import sys
import math


def combination(n, m):
    return math.factorial(m) // (math.factorial(n) * math.factorial(m-n))


t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    print(combination(n, m))