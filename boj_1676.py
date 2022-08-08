#1676번: 팩토리얼 0의 개수

"""
import sys
import math

n = int(sys.stdin.readline())

fac = (str(math.factorial(n)))

count = 0
for i in range(len(fac)):
    if fac[len(fac)-i-1] == '0':
        count += 1
        continue
    else: break
print(count)
"""

import sys
import math

fac = (str(math.factorial(int(sys.stdin.readline()))))
print(len(fac) - len(str(int(fac[::-1]))))