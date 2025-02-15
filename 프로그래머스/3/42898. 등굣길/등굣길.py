def solution(m, n, puddles):
    dp = [[0] * (m+1) for i in range(n+1)]
    dp[1][1] = 1
    for x, y in puddles:
        dp[y][x] = -1
    for j in range(1, n+1):
        for k in range(1, m+1):
            if dp[j][k] == -1:
                dp[j][k] = 0
            else:
                # 위쪽과 왼쪽을 더해야 오른쪽과 아래쪽으로만 움직인게됨
                dp[j][k] += (dp[j-1][k] + dp[j][k-1])
    return dp[n][m] % 1000000007