import sys
def input():
    return sys.stdin.readline().rstrip()
def sol(c,h):
    if dp[c][h] != INF:
        return dp[c][h]
    temp = h
    for down in range(1,h):
        temp = min(temp,max(sol(c-1,down-1),sol(c,h-down)) + 1)
    dp[c][h] = temp
    return dp[c][h]

P = int(input())

INF = float('inf')
dp = [[INF if i != 1 else h  for h in range(1001)] for i in range(51)]
for i in range(1,51):
    dp[i][1] = 1
for _ in range(P):
    count, height = map(int,input().split())

    
    print(sol(count,height))