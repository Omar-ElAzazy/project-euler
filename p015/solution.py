N = 20
dp = [1] * (N + 1)
for x in range(N):
	for y in range(N - 1, -1, -1):
		dp[y] = dp[y] + dp[y + 1]
print(dp[0])

