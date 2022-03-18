import sys


def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

dp = [[float('inf') for _ in range(3)]] + [[i]*3 for i in map(int,input().split())]  + [[float('inf') for _ in range(3)]]


for _ in range(N-1):
    next_ = [float('inf')] + list(map(int,input().split())) + [float('inf')]

    temp_dp = [[float('inf') for _ in range(3)]] + [[float('inf')]*3 for i in range(M) ]  + [[float('inf') for _ in range(3)]]
    # -1,0,1
    for col in range(1,M+1):
        temp_dp[col][0] = min(dp[col-1][1] , dp[col-1][2]) + next_[col]
        temp_dp[col][1] = min(dp[col][0] , dp[col][2]) + next_[col]
        temp_dp[col][2] = min(dp[col+1][0] , dp[col+1][1]) + next_[col]
    dp = temp_dp


result = float('inf')
for row in dp:
    result = min(result,min(row))

print(result)
       
