from itertools import permutations

import sys
input = sys.stdin.readline
def rotate(command,moving_arr):
    global arr
    cnt = 1
    while cnt<=command[2]:
        start_row,start_col = command[0]-cnt, command[1]-cnt
        end_row,end_col = command[0] + cnt,command[1] + cnt
        for row in range(start_row,end_row+1):
            if row == start_row or row == end_row:
                if row == start_row:
                    for col in range(start_col,end_col+1):
                        if col == end_col:
                            moving_arr[row+1][col] = prev_arr[row][col]
                        else:
                            moving_arr[row][col+1] = prev_arr[row][col]
                else:
                    for col in range(end_col,start_col-1,-1):
                        if col == start_col:
                            moving_arr[row-1][col] = prev_arr[row][col]
                        else:
                            moving_arr[row][col-1] = prev_arr[row][col]
            else:
                moving_arr[row-1][start_col] = prev_arr[row][start_col]
                moving_arr[row+1][end_col] = prev_arr[row][end_col]
        cnt += 1


N,M,K = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
command_list = []
for _ in range(K):
    x,y,r = map(int,input().split())
    command_list.append((x-1,y-1,r))
result = float('inf')

for commands in permutations(command_list):
    move_arr = [row[:] for row in arr]
    prev_arr = [row[:] for row in arr]
    for command in commands:
        rotate(command,move_arr)
        prev_arr = [row[:] for row in move_arr]
    arr_min = min(list(map(sum,move_arr)))
    result = min(arr_min,result)
print(result)