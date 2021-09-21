import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
v = [0]+[int(input()) for _ in range(N)]

dp = [[v[i] *N  if i == j else 0 for i in range(N+1)] for j in range(N+1)]



for y in range(1,N+1):
    for x in range(y-1,0,-1):
        dp[x][y] = max(dp[x+1][y] + v[x] * (N - y + x), dp[x][y-1] + v[y]*(N-y+x))

print(dp[1][N])
