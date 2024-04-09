import math

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

total = 0
for i in range(n):
    tester_num = a[i]
    if b >= tester_num:
        total += 1
        continue
    else:
        tester_num -= b
        # print(tester_num / c)
        d = math.ceil(tester_num / c)
        # print(d)
        total += d + 1

print(total)
