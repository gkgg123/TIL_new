import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = [0]+list(map(int,input().split()))

M = int(input())

for i in range(1,N+1):
    arr[i] += arr[i-1]

dp = [[0 for _ in range(N+1)] for _ in range(4)]

for train in range(1,4):
    for x in range(M*train,N+1):
        dp[train][x] = max(dp[train][x-1],dp[train-1][x-M]  + arr[x]-arr[x-M])


print(dp[3][N])