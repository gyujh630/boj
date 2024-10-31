import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * 3 for _ in range(N)]
dp[0] = arr[0] # 항상 이게 최선

# dp[i-1][n] -> 이전 단계에서 n번째 집을 골랐으며 그 이전에는 뭘 골랐는지 모르겠지만, 이전 단계에 n번쨰 집을 고른 경우에서는 최솟값을 보장함


for i in range(1, N):
    # 현재 선택하는 값 + 이전 단계에서 가능한 값들 중 최솟값
    dp[i][0] = arr[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[-1]))