#설탕배달

import sys

n = int(sys.stdin.readline())
flag = 0
for i in range(n//3 + 1):
    three = 3*i
    five = (n - three)/5
    if five == int(five):
        print(int(i+five))
        flag = 1
        break
if flag == 0:
    print(-1)