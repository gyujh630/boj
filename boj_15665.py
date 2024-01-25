# 15665번: N과 M(11)

import sys


def func(select):
    if len(select) == m:
        print(*select)
        return
    for i in range(len(a)):
        select.append(a[i])
        func(select)
        select.pop()


n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
a = sorted(list(set(a)))

for i in range(len(a)):
    func([a[i]])