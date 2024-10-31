import sys

N = int(sys.stdin.readline())
dp = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))

for i in range(1, N):
    for j in range(0, i+1):
        if j == 0:
            dp[i][j] += dp[i-1][0]
        elif j == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])

print(max(dp[N-1]))
'''
dp
위에서 아래로 가며 선택
첫 번째(root)는 항상 고정(예제에서 7)
두 번째 부터는 위 선택값의 왼쪽, 오른쪽 중 더 큰 값을 선택
dp[i][j]

'''