import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = arr[0]

for i in range(1, N):
    # 현재 선택하는 값 + 이전 단계에서 가능한 값들 중 최솟값
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))