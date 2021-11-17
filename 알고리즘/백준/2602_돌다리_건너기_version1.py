import sys

def input():
    return sys.stdin.readline().rstrip()

S = list(input())
D = list(input())
A = list(input())
N = len(A)
M = len(S)
dp = [[1  if k == 0 else 0 for k in range(len(S)+1)] for _ in range(2)]

for x in range(N):
    for y in range(M-1,-1,-1):
        if D[x] == S[y]:
            dp[0][y+1] += dp[1][y]
        if A[x] == S[y]:
            dp[1][y+1] += dp[0][y]

print(dp[1][M] + dp[0][M])