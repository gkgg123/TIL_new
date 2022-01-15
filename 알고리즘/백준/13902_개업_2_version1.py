import sys

def input():
    return sys.stdin.readline().rstrip()



N,M = map(int,input().split())

S = list(map(int,input().split()))

INF = float('inf')
dp = [INF for _ in range(N+1)]

for ind1 in range(M-1):
    for ind2 in range(ind1+1,M):
        v = S[ind1] + S[ind2]
        if v>N:
            continue
        S.append(v)
S = list(set(S))
dp[0] = 0
for size in S:

    for prev in range(N-size+1):
        dp[prev+size] = min(dp[prev+size],dp[prev]+1)

if dp[N] == INF:
    print(-1)
else:
    print(dp[N])