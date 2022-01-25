import sys


def input():
    return sys.stdin.readline().rstrip()


N,M,H = map(int,input().split())


dp = [[0  for t in range(H+1)] for _ in range(N+1)]
dp[0][0] = 1
arr = [list(map(int,input().split())) for _ in range(N)]


for person in range(1,N+1):
    for coin in [*arr[person-1],0]:
        for prev in range(H-coin,-1,-1):
            if dp[person-1][prev]:
                dp[person][prev+coin] += dp[person-1][prev]

print(dp[N][H]%10007)