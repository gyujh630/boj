# 6603번: 로또

import sys

def func(select):
    if len(select) == 6:
        print(*select)
        return
    for i in range(1, len(s)):
        if s[i] not in select and select[-1] <= s[i]:
                select.append(s[i])
                func(select)
                select.pop()

while True:
    s = sys.stdin.readline().rstrip()
    if s == '0':
        break
    s = list(map(int, s.split()))
    k = s[0]
    s = s[1:]
    for i in range(k-5):
        func([s[i]])
    print('')
