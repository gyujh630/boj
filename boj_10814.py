#시간 초과 풀이
"""
import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(sys.stdin.readline().split())
b = a.copy()
a = sorted(a)
for i in range(len(a)):
    if i == 0: continue
    if int(a[i-1][0]) == int(a[i][0]) and b.index(a[i]) < b.index(a[i-1]):
        a[i] ,a[i-1] = a[i-1], a[i]

for i in range(len(a)):
    print(a[i][0], a[i][1])
"""

#틀린 풀이 (나이 str)
"""
import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append((sys.stdin.readline().split()))

a.sort(key = lambda x : x[0])

for i in range(len(a)):
    print(a[i][0], a[i][1])
"""

#맞은 풀이 (나이를 int로 변경)
import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    age, name = sys.stdin.readline().split()
    age = int(age)
    a.append([age, name])

a.sort(key = lambda x : x[0])

for i in range(len(a)):
    print(a[i][0], a[i][1])




