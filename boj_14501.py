# 삼성 역량테스트 준비
# 백준 14501번: 퇴사

'''

상담 1회 = Ti의 날짜 소요, Pi의 수입


'''


def func(ck, money, now):
    global maxi
    if now >= n:
        maxi = max(maxi, money)
        return

    # dfs
    for i in range(now, len(ck)):
        ti = table[i][0]
        pi = table[i][1]

        if i + ti <= n:
            if ck[i] == 0:
                ck[i] = 1  # 체크
                func(ck, money + pi, i + ti)
                ck[i] = 0
        else:
            maxi = max(maxi, money)






n = int(input())
table = []
maxi = 0
for _ in range(n):
    table.append(list(map(int, input().split())))


check = [0] * len(table)
func(check, 0, 0)
print(maxi)