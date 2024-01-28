# 15666번: N과 M (12)

import sys


def func(select):
    if len(select) == m:
        print(*select)
        return
    for j in range(len(a)):
        if a[j] >= select[-1]:
            select.append(a[j])
            func(select)
            select.pop()


n, m = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
a = list(a)
a.sort()


for i in range(len(a)):
    func([a[i]])