# 삼성 SW 역량테스트 준비
# 백준 14890번: 경사로


N, L = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

total = 0


def rotate(matrix):
    new_matrix = []
    for i in range(N):
        a = []
        for j in range(N):
            a.append(matrix[j][i])
        new_matrix.append(a)

    return new_matrix


def check(line):
    installed = [False] * N
    for j in range(1, N):
        diff = line[j] - line[j - 1]
        if abs(diff) > 1:
            return False
        if diff == 1:
            if j - L < 0:
                return False
            for k in range(L):
                if line[j - 1 - k] != line[j - 1] or installed[j - 1 - k]:
                    return False
                installed[j - 1 - k] = True  # 경사로 설치 표시
        elif diff == -1:
            if j + L > N:
                return False
            for k in range(L):
                if line[j + k] != line[j] or installed[j + k]:
                    return False
                installed[j + k] = True  # 경사로 설치 표시
    return True



count = 0
for i in range(N):
    if check(matrix[i]):
         count += 1

matrix = rotate(matrix)

for i in range(N):
    if check(matrix[i]):
        count += 1


print(count)