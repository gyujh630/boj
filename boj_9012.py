#9012번: 괄호

import sys

def test():
    n = sys.stdin.readline().rstrip()
    a = list(n)
    right = 0
    left = 0
    for i in range(len(a)):
        if a.pop() == ')':
            right += 1
        else: left += 1
        if right < left:
            return 1
    return right - left

t = int(sys.stdin.readline())
for i in range(t):
    if test() == 0:
        print('YES')
    else: print('NO')