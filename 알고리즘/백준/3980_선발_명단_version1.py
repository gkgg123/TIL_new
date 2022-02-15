import sys

def input():
    return sys.stdin.readline().rstrip()


def dfs(idx,val):
    global result
    if idx == 11:
        if result < val:
            result = val
        return
    for ind in range(11):
        if arr[idx][ind] and visited[ind]:
            visited[ind] = False
            dfs(idx+1,val+arr[idx][ind])
            visited[ind] = True
        

T = int(input())

for _ in range(T):
    result = 0

    visited = [True for _ in range(11)]

    arr = [list(map(int,input().split())) for _ in range(11)]


    dfs(0,0)
    print(result)