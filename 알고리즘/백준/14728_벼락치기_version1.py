import sys

def input():
    return sys.stdin.readline().rstrip()


N,T = map(int,input().split())

dp = [0 for _ in range(T+1)]


arr = [list(map(int,input().split())) for _ in range(N)]

for time,val in arr:
    for prev_time in range(T-time,-1,-1):
        dp[prev_time+time] = max(dp[prev_time+time],dp[prev_time] + val)
    

print(max(dp))