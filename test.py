# 삼성 문제 대비


arr1 = [[1,2,3],[4,5,6],[7,8,9]]

print('기본')
for a in arr1:
    print(a)
print()


# 행렬 전환 (전치)
print('전치')
arr2 = list(map(list, zip(*arr1)))

for a in arr2:
    print(a)
print()


print('시계방향 90도 회전')
# 시계 90도 회전 / 전치 후 뒤집기
arr3 = list(map(list, zip(*arr1)))
arr3 = [list(row)[::-1] for row in arr3]

for a in arr3:
    print(a)
print()



print('반시계방향 90도 회전')
# 반시계 90도 회전 / 전치 후 뒤집기
arr4 = list(map(list, zip(*arr1)))
arr4 = [list(row) for row in arr4][::-1]

for a in arr4:
    print(a)
print()