#10773번: 제로

import sys
k = int(sys.stdin.readline())
a = []
for i in range(k):
    num = int(sys.stdin.readline().rstrip())
    if num != 0:
        a.append(num)
    else:
        a.pop()
print(sum(a))