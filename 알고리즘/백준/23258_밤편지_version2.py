import sys

def input():
    return sys.stdin.readline().rstrip()

N,Q = map(int,input().split())

INF = float('inf')

arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i != j and arr[i][j] == 0:
            arr[i][j] = INF


dp = [[row[:] for row in arr]]

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if arr[start][end] > arr[start][mid] + arr[mid][end]:
                arr[start][end] = arr[start][mid] + arr[mid][end]

    dp.append([row[:] for row in arr])
answer = []
for _ in range(Q):
    C,s,e = map(int,input().split())
    result = dp[C-1][s-1][e-1]
    answer.append(str(-1) if result == INF else str(result))

sys.stdout.write('\n'.join(answer))