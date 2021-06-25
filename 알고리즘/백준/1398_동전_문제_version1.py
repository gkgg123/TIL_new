import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
dp = [i for i in range(101)]

for i in range(100):
    for coin in [10,25]:
        if i +coin > 100:continue
        dp[i+coin] = min(dp[i+coin],dp[i]+1)
for _ in range(T):
    N = int(input())

    answer = 0
    while N>0:
        answer += dp[N%100]
        N//=100
    print(answer)



