import sys
def t():
    n = int(sys.stdin.readline())
    n_set = set(map(int, sys.stdin.readline().split()))

    m = int(sys.stdin.readline())
    m_list = list(map(int, sys.stdin.readline().split()))

    for i in m_list:
        if i in n_set:
            print('1', end=' ')
        else:
            print('0', end=' ')

t()
