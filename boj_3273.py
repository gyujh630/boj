#3273번: 두 수의 합

#성공: 투포인터
import sys

n = int(sys.stdin.readline())
a = sorted(list(map(int, sys.stdin.readline().split(" "))))
x = int(sys.stdin.readline())
count = 0

left = 0
right = n-1

while left < right:
    temp = a[left] + a[right]
    if temp == x:
        count += 1
        left += 1
    elif temp > x:
        right -= 1
    else: left += 1

print(count)


# 성공 (in 사용)
# import sys
#
# n = int(sys.stdin.readline())
# a = set(map(int, sys.stdin.readline().split(" ")))
# x = int(sys.stdin.readline())
# count = 0
#
#
# for i in a:
#     j = x - i
#     if j in a:
#         count += 1
#
# print(int(count/2))


# 실패 (시간초과)
# import sys
#
# n = int(sys.stdin.readline())
# a = list(map(int, sys.stdin.readline().split(" ")))
# x = int(sys.stdin.readline())
# count = 0
#
# for i in a:
#     for j in a:
#         if i+j == x:
#             count += 1
#
# print(int(count/2))