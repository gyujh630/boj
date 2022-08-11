# 11478번: 서로 다른 부분 문자열의 개수

import sys

s = sys.stdin.readline().rstrip()
s_set = set()
for i in range(len(s)):
    for j in range(len(s)   ):
        s_set.add(s[i : j+1])
print(len(s_set)-1)