import sys
def input():
    return sys.stdin.readline().rstrip()

def solution():
    for k in arr:
        k = k%7
        dp[1][k] = 1
        for prev in range(7):
            if dp[0][prev]:
                dp[1][(prev+k)%7] = 1
                dp[1][prev] = 1
        if dp[1][4]:
            return 'YES'
        dp[0] = dp[1][:]
        dp[1] = [0 for _ in range(7)]
    return 'NO' 

N = int(input())

arr = list(map(int,input().split()))
arr.sort()

dp = [[0 for _ in range(7)] for _ in range(2)]
print(solution())
