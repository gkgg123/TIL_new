import sys

def input():
    return sys.stdin.readline().rstrip()

L,N = map(int,input().split())
# 길이 용량
arr = [list(map(int,input().split())) for _ in range(N)]


dp = [0 for _ in range(L+1)]
for i in range(N):
    ml,mc = arr[i]
    for l in range(L,-1,-1):
        if dp[l] != 0 and l+ml <=L:
            dp[l+ml] = max(dp[l+ml],min(dp[l],mc))
    if ml<=L:
        dp[ml] = max(dp[ml],mc)
print(dp[L])