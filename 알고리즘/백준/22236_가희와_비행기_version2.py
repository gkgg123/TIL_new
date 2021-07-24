import sys

def input():
    return sys.stdin.readline().rstrip()



d,m = map(int,input().split())
d//=2
d-=1
dp = [0 for _ in range(d+1)]
dp[0] = 1

for i in range(1,d+1):
    for j in range(0,i):
        dp[i] = (dp[i] + dp[j]*dp[i-j-1])%m
        print(j,i-j-1)
    print('--')

print(dp[d])