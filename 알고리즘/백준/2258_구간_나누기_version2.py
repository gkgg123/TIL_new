import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

arr = [0]+ [int(input()) for _ in range(N)]

dp_unselct = [[-float('inf') for _ in range(M+1)] for _ in range(N+1)]
dp_select = [[-float('inf') for _ in range(M+1)] for _ in range(N+1)]
dp_unselct[1][0] = 0
dp_select[1][1] = arr[1]
for i in range(2,N+1):
    dp_unselct[i][0] = 0
    for k in range(1,M+1):
        dp_unselct[i][k] = max(dp_unselct[i-1][k],dp_select[i-1][k])
        dp_select[i][k] = max(dp_unselct[i-1][k-1] + arr[i],dp_select[i-1][k] + arr[i])
print(max(dp_select[N][M],dp_unselct[N][M]))
