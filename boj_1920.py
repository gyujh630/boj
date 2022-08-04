import sys

def test(n):
    a = set(map(int, sys.stdin.readline().split()))
    m, b = int(sys.stdin.readline()), list(map(int, sys.stdin.readline().split()))
    for i in b:
        if i in a:
            print(1)
        else: print(0)

test(int(sys.stdin.readline()))