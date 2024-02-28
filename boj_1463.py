# 1463번: 1로 만들기

import sys

X = int(sys.stdin.readline())

dp = [0] * (X + 1)

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[X])