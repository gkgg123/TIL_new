import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())
prefix_sum = [[0 for _ in range(2010)] for _ in range(2010)]
result = [[0 for _ in range(2010)] for _ in range(2010)]
arr = [[0]+list(map(int,input().split()))+[0] for _ in range(N)]
arr = [[0 for _ in range(N+2)]] + arr + [[0 for _ in range(N+2)]]
for x in range(1,N+1):
    for y in range(1,N+1):
        prefix_sum[x][y] += prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1]

        bomb = -(arr[x][y] + prefix_sum[x][y])
        if bomb>0:
            result[x+M//2][y+M//2] = bomb
            prefix_sum[x][y] += bomb
            prefix_sum[x+M][y] -= bomb
            prefix_sum[x][y+M] -= bomb
            prefix_sum[x+M][y+M] += bomb



for x in range(1,N+1):
    print(*result[x][1:N+1])

            