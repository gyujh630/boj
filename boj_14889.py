# 삼성 sw역량테스트 준비
# 백준 14889번: 스타트와 링크

# 8(n) -> 4(n/2) vs 4 .. (a,b)(c,d) vs (e,f)(g,h)..

# 테이블 안에서.. 아무거나 네개를 고른다. 어차피 브루트포스이므로. [2,3,6,9] 과 같이 나왔다면 앞 절반까지인 2,3 을 합, 뒤 절반인  6,9 합 비교
# 능력치의 범위는 1 <= s <= 100이다


# 1,4,5 면? 14 41 15 51 45 54

import sys

def func(depth, idx, visited):
    global mini
    if depth == n//2:

        s_total = 0
        l_total = 0

        for i in range(n-1):
            for j in range(i+1,n):
                if i < j:
                    if visited[i] and visited[j]:
                        s_total += s[i][j]
                        s_total += s[j][i]
                    elif not visited[i] and not visited[j]:
                        l_total += s[i][j]
                        l_total += s[j][i]

        mini = min(abs(s_total - l_total), mini)
        if mini == 0:
            print(0)
            exit(0)
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            func(depth + 1, i+1, visited)
            visited[i] = False


n = int(sys.stdin.readline())
s = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

mini = 100*n
visited = [False] * n
func(0, 0, visited)

print(mini)

