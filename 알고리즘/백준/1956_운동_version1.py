import sys

def input():
    return sys.stdin.readline().rstrip()

V,E = map(int,input().split())
INF = float('inf')
dp  = [[INF if i != j else 0 for i in range(V+1)] for j in range(V+1)]
for _ in range(E):
    x,y,pay = map(int,input().split())
    dp[x][y] = pay


for mid in range(1,V+1):
    for start in range(1,V+1):
        for end in range(1,V+1):
            if dp[start][end] > dp[start][mid] + dp[mid][end]:
                dp[start][end] = dp[start][mid] + dp[mid][end]

result = INF
for x in range(1,V+1):
    for y in range(1,V+1):
        if x ==y:continue
        result = min(result,dp[x][y] + dp[y][x])

print(-1 if result == INF else result)