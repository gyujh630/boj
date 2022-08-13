import sys
n = int(sys.stdin.readline())
a = []
for i in range(n):
    b = input()
    if b not in a:
        a.append(b)

c = []
for i in range(len(a)):
    c.append([len(a[i]) ,a[i]])
c = sorted(c)
for i in range(len(c)):
    print(c[i][1])

"""
#좋은 풀이
import sys

tmp = set()
for i in range(int(input())):
    tmp.add(sys.stdin.readline().rstrip())
a = sorted(tmp, key=lambda x: (len(x), x))
print('\n'.join(a))
"""