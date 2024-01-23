#15649번: N과 M(1)

import sys

def find_sequence(select, n, m):
    if len(select) == m:
        print(*select)
    for i in range(1, n+1):
        if i not in select:
            select.append(i)
            find_sequence(select, n, m)
            select.pop()

    return

n, m = map(int, sys.stdin.readline().split())

find_sequence([], n, m)
