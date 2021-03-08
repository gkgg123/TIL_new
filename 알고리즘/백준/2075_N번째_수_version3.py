
# stkang9409 풀이 해석

def find_max_value(x):
    return arr[max_row_list[x]][x]

import sys

input = sys.stdin.readline


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]

max_row_list = [N-1]*N
# 각 열마다 가장 큰 값은 N-1번 행에 있는 값이다.
# 매번 돌면서 각 열마다 가장 큰값들을 비교해, 가장 큰 값이 있는 열의 index 값을 하나씩 줄여나간다.
# 그렇게 하면 마지막 N번째에 가장 큰 값을 가지는 열의 값이 N번째로 큰 수의 열값이 되고
# 그 때 저장된 위치의 값이 행이된다.
for cnt in range(N):
    max_col_index = 0
    for col in range(N):
        max_col_index = max(col,max_col_index,key= find_max_value)
    if cnt == N-1:
        print(arr[max_row_list[max_col_index]][max_col_index])
    max_row_list[max_col_index] -= 1