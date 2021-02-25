def dfs(W,H):
    if W == 0:
        return 1
    if dp[W][H]:
        return dp[W][H]
    dp[W][H] = dfs(W-1,H+1)
    if H>0:
        dp[W][H] += dfs(W,H-1)
    return dp[W][H]


dp = [[0]*31 for _ in range(31)]

for i in range(1,31):
    dfs(i,0)

while True:
    N = int(input())

    if not N:
        break
    print(dp[N][0])