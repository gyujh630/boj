#10816번: 숫자 카드 2

import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))

dict = {}
for i in n_list:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

n_set = set(n_list)

m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

for i in m_list:
    if i in n_set:
        print(dict[i], end = ' ')
    else:
        print(0, end =' ')
