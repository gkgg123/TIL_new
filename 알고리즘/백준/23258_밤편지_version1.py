import sys

def input():
    return sys.stdin.readline().rstrip()

N,Q = map(int,input().split())

INF = float('inf')
dp = [[[INF if i!=j else 0 for _ in range(N+1)] for i in range(N+1)] for j in range(N+1)]
for x in range(1,N+1):
    temp = [0]+list(map(int,input().split()))
    for y in range(1,N+1):
        if x == y:continue
        if temp[y]:
            dp[x][y][0] = temp[y]

for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            dp[start][end][mid] =  min(dp[start][end][mid],dp[start][end][mid-1],dp[start][mid][mid-1] + dp[mid][end][mid-1])
answer = []
for _ in range(Q):
    C,s,e = map(int,input().split())
    result = dp[s][e][C-1]
    if result == INF:
        answer.append(str(-1))
    else:
        answer.append(str(result))
sys.stdout.write('\n'.join(answer))
