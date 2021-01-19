import sys
def check():
    global N,H
    for ind in range(N):
        current_ind = ind
        for k in range(H):
            current_ind += visited[k][current_ind]
        if current_ind != ind:
            return False
            
    return True




def dfs(ladder_index,cnt,limit):
    global N,H,result
    if limit == cnt:
        if check():
            result = limit
        return
    for ind in range(ladder_index,N*H):
        row_index = ind//N
        col_index = ind%N
        if col_index == N-1:
            continue
        if not visited[row_index][col_index] and not visited[row_index][col_index+1]:
            visited[row_index][col_index] = 1
            visited[row_index][col_index+1] = -1
            dfs(ind+2,cnt+1,limit)
            if result != 4:
                return
            visited[row_index][col_index] = 0
            visited[row_index][col_index+1] = 0





N,M,H = map(int,input().split())
# H는 놓을 수 있는 개수
# M 은 가로선의 개수
# 앞은 가로선의 위치 뒤는 2개의 위치
if M == 0:
    print(0)
else:
    result = 4
    call = 0
    visited = [[0]*N for _ in range(H)]
    for _ in range(M):
        row,node = map(int,sys.stdin.readline().split())
        visited[row-1][node-1] = 1
        visited[row-1][node] = -1

    if check():
        print(0)
    else:
        for k in range(1,4):
            dfs(0,0,k)
            if result != 4:
                break
        if result != 4:
            print(result)
        else:
            print(-1)