# 삼성 SW 역량 테스트 준비
# 백준 15686번: 치킨 배달


# 집 개수 최댓값 : 200개
# 폐업시키지 않을 치킨집 개수 M <= 치킨집 개수


min_distance = int(1e9)


# 도시의 치킨 거리 구하는 함수
def get_city_chicken_distance(select):
    chicken_dt = 0
    for home in home_list:
        mini = int(1e9)
        for ch in select:
            mini = min(mini, abs(home[0] - ch[0]) + abs(home[1] - ch[1]))
        chicken_dt += mini
    return chicken_dt


def backtracking(start, depth, select):
    global min_distance
    if depth == m:
        print('oh')
        min_distance = min(min_distance, get_city_chicken_distance(select))
        return

    for i in range(start, len(chicken_list)):
        if chicken_list not in select:
            select.append(chicken_list[i])
            backtracking(i + 1, depth + 1, select)
            select.pop()


n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]

# 집 리스트, 치킨집 리스트 구하기
home_list = []
chicken_list = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home_list.append((i, j))
        elif city[i][j] == 2:
            chicken_list.append((i, j))

# 폐업시킬 매장 수
delete_num = len(chicken_list) - m


backtracking(0, 0, [])  # 없앨 매장을 고르기

print(min_distance)
