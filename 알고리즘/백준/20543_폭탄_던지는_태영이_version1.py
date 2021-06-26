import sys

def input():
    return sys.stdin.readline().rstrip()

def calc_prefix(x,y,C=0):
    prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] - prefix_sum[x-1][y-1] + C
N,M = map(int,input().split())

K = M//2

arr = [list(map(int,input().split())) for _ in range(N)]

result = [[0 for _ in range(N)] for _ in range(N)]
prefix_sum = [[0 for _ in range(N)] for _ in range(N)]
                    
for x in range(N):
    for y in range(N):
        if x+K >=N or y+K >=N:continue
        calc_prefix(x+K,y+K,result[x+K][y+K])
        right_x,right_y = x+K,y+K
        left_x,left_y = max(x-K,1),max(y-K,1)
        prev_bomb = prefix_sum[right_x][right_y] - prefix_sum[left_x-1][right_y] - prefix_sum[right_x][left_y-1] + prefix_sum[left_x-1][left_y-1]
        result[right_x][right_y] = -arr[x][y] -prev_bomb
        calc_prefix(x+K,y+K,result[right_x][right_y])

for row in result:
    print(*row) 