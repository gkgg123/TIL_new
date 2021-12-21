import sys

def input():
    return sys.stdin.readline().rstrip()


N,W = map(int,input().split())


dp = [[0 for _ in range(W+1)] for _ in range(N)]

first = int(input())

if first == 1:
    dp[0][0] = 1
else:
    dp[0][1] = 1


for ind in range(1,N):
    num = int(input())
    num -= 1
    dp[ind][0] = dp[ind-1][0]
    if not num:
        dp[ind][0] += 1
    for j in range(1,W+1):
        dp[ind][j] = max(dp[ind-1][j],dp[ind-1][j-1])
        if j%2 == num:
            dp[ind][j] += 1

print(max(dp[N-1]))
