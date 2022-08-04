#18870번: 좌표 압축

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
new_a = sorted(set(a))                                 #a를 set으로 만들고 정렬한, new_a를 생성
dictionary = {new_a[i] : i for i in range(len(new_a))} #딕셔너리에 '숫자 : new_a에서의 인덱스'로 저장

for i in a:                          #기존 a를 돌며
    print(dictionary[i], end = ' ')  #a[i] key에 해당하는 dictionary의 value를 출력

"""
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

b = sorted(set(a))

for i in a:
    print(b.index(i))
"""


"""
import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

for i in a:
    count = 0
    for j in set(a):
        if i > j:
            count += 1
    print(count, end = " ")
"""

