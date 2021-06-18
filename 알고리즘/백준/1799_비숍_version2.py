# chw0501님 코드 복기

import sys

def input():
    return sys.stdin.readline()

def dfs(left_slash_num):
    if visited[left_slash_num]:
        return 0 
    visited[left_slash_num] = True

    for right_slash_num in slash_dict[left_slash_num]:
        if right_slash[right_slash_num] == -1 or dfs(right_slash[right_slash_num]):
            left_slash[left_slash_num] = right_slash_num
            right_slash[right_slash_num] = left_slash_num
            return 1
    return 0

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
right_slash = [-1 for _ in range(2*N+1)]
left_slash = [-1 for _ in range(2*N+1)]
slash_dict = [[] for _ in range(2*N+1)]
for x in range(N):
    for y in range(N):
        if arr[x][y]:
            slash_dict[x+y].append(x-y+N)


result = 0
for left_slash_num in range(2*N):
    visited = [False for _ in range(2*N)]
    if dfs(left_slash_num):
        result += 1
print(result)