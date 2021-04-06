from itertools import permutations

import sys
input = sys.stdin.readline


def rotate(command,move_arr):
    x,y,s = command
    for i in range(1,s+1):
        subtract_data = move_arr[x-i][y-i] # 좌측 최상단 꼭지점을 빼놓기
        for r in range(x-i,x+i): # 좌측 세로를 아래에서 위로 올리는 과정
            move_arr[r][y-i] = move_arr[r+1][y-i]
        for c in range(y-i,y+i):
            move_arr[x+i][c] = move_arr[x+i][c+1]
        for r in range(x+i,x-i,-1):
            move_arr[r][y+i] = move_arr[r-1][y+i]
        for c in range(y+i,y-i+1,-1):
            move_arr[x-i][c] = move_arr[x-i][c-1]
        move_arr[x-i][y-i+1] = subtract_data
        





N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
command_list = []
for _ in range(K):
    x,y,r = map(int,input().split())
    command_list.append((x-1,y-1,r))
result = float('inf')


for commands in permutations(command_list):

    move_arr = [row[:] for row in arr]
    for command in commands:
        rotate(command,move_arr)
    arr_min = min(list(map(sum,move_arr)))
    result = min(arr_min,result)
print(result)