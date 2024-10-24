from collections import deque

n = int(input())
a = []
for i in range(n):
    a.append(i+1)

a = deque(a)

while len(a) > 1:
    a.popleft()
    left = a.popleft()
    a.append(left)

print(a[0])
