import sys

def test():
    n, m = map(int, sys.stdin.readline().split())
    s = set()
    for _ in range(n):
        s.add(sys.stdin.readline().strip())

    count = 0
    for _ in range(m):
        voca = sys.stdin.readline().strip()
        if voca in s:
            count += 1

    print(count)

test()