import sys

N = int(sys.stdin.readline())

info = []
for n in range(N):
    info.append(list(map(int, sys.stdin.readline().split())))

info.sort()
result = [info[0]]
info.pop(0)
for i in info:
    # result의 마지막 값 빼기
    br_start = result[-1][0]
    br_end = result[-1][1]
    cur_start = i[0]
    cur_end = i[1]

    if cur_start < br_end and cur_end < br_end:  # 교체
        result.pop()
        result.append(i)
    elif cur_start >= br_end:  # 추가
        result.append(i)

print(len(result))