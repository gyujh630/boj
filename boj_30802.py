import sys

n = int(sys.stdin.readline())
size_arr = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

count = 0
for i in size_arr:
    if i == 0:
        continue
    elif i <= t:
        count += 1
    else:
        tmp = i % t
        if tmp == 0:
            count += i // t
        else:
            count += i // t + 1

print(count)
print(n // p, n % p)