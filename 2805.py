#나무 자르기

import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
left = 0
right = max(a)
result = 0

while left <= right:
    count = 0
    mid = (left + right) // 2
    for tree in a:
        if tree > mid:            #해당 나무가 절단기 높이보다 높은 경우에만
            count += (tree - mid)      #해당 나무에서 절단기 높이를 뺀 만큼을 더해줌(잘린 나무의 높이)
            if count >= m:             #추가하는 중에 이미 구할 나무(m)을 초과해버린 경우 break
                break
    if count >= m:                #자를 양보다 많이 자르거나 딱 맞추어 자른 경우
        result = mid                  #result값에 현재 절단기 높이(mid) 할당
        left = mid + 1                #우측으로 범위 축소(절단기를 높여야 함)
    else:                         #자를 양보다 적게 자른 경우 (문제 조건 위배)
        right = mid - 1               #좌측으로 범위 축소(절단기를 낮춰야 함)

print(result)



