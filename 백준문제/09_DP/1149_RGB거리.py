N = int(input())
houses = [0]*N
min_result = 10000000

for i in range(N):
    houses[i] = list(map(int, input().split()))
dp = [[0]*3 for _ in range(N+1)]

for i in range(1, N+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + houses[i-1][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+ houses[i-1][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + houses[i-1][2]

print(min(dp[-1]))