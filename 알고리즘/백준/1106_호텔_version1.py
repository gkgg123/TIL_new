import sys

def input():
    return sys.stdin.readline().rstrip()



C,N = map(int,input().split())

dp = [float('inf') for i in range(C+1)]
dp[0] = 0

for x in range(N):
    pay,person = map(int,input().split())

    prev = 0
    while prev<=C:
        if dp[prev] != float('inf'):
            if prev + person > C:
                dp[C] = min(dp[C],dp[prev]+pay)
            else:
                dp[prev+person] = min(dp[prev+person], dp[prev]+ pay)
        prev += 1

print(dp[C])