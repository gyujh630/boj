# 1759번: 암호 만들기

import sys


def func(select, consonant, vowel):
    if len(select) == l and vowel >= 1 and consonant >= 2:
        print(''.join(map(str, select)))
    for i in range(1, c):
        if a[i] not in select and a[i] > select[-1]:
            select.append(a[i])
            if a[i] in vowels:
                vowel += 1
                func(select, consonant, vowel)
                vowel -= 1
            else:
                consonant += 1
                func(select, consonant, vowel)
                consonant -= 1
            select.pop()


l, c = map(int, sys.stdin.readline().split())
a = list(sys.stdin.readline().split())
a = sorted(a)

vowels = ['a', 'e', 'i', 'o', 'u']
for i in range(c - l + 1):
    if a[i] in vowels:
        func([a[i]], 0, 1)
    else:
        func([a[i]], 1, 0)
