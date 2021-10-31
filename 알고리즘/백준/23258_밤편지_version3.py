import sys

def input():
    return sys.stdin.readline().rstrip()

N,Q = map(int,input().split())

dp = [list(map(int,input().split())) for _ in range(N)]

INF = float('inf')
for x in range(N):
    for y in range(N):
        if dp[x][y] == 0 and x !=y:
            dp[x][y] = INF

querys = []
answer = [-1 for _ in range(Q)]
for idx in range(Q):
    C,S,E = map(int,input().split())
    querys.append((C-1,S-1,E-1,idx))


querys.sort()

cur_count = 0

for c,s,e,idx in querys:
    while cur_count<c:
        for start in range(N):
            for end in range(N):
                if dp[start][end] > dp[start][cur_count] + dp[cur_count][end]:
                    dp[start][end] = dp[start][cur_count] + dp[cur_count][end]

        cur_count += 1
    
    answer[idx] = str(-1) if dp[s][e] == INF else str(dp[s][e])

sys.stdout.write('\n'.join(answer))