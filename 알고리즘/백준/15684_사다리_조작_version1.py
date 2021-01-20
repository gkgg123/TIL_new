def check():
    global N,H
    for ind in range(N):
        current_ind = ind
        for k in range(H):
            if visited[k][current_ind]:
                current_ind += 1
            elif current_ind>0 and visited[k][current_ind-1]:
                current_ind -= 1
        if current_ind != ind:
            return False
            
    return True




def dfs(row_index,col_index,cnt,limit):
    global N,H,result
    if cnt == limit:
        if check():
            result = cnt
        return
    for k in range(row_index,H):
        if k == row_index:
            search_y = col_index
        else:
            search_y = 0
        for y in range(search_y,N-1):
            if not visited[k][y] and not visited[k][y+1]:
                visited[k][y] = 1
                dfs(k,y+2,cnt+1,limit)
                visited[k][y] = 0









N,M,H = map(int,input().split())
# H는 놓을 수 있는 개수
# M 은 가로선의 개수
# 앞은 가로선의 위치 뒤는 2개의 위치
result = float('inf')
visited = [[0]*N for _ in range(H)]
for _ in range(M):
    row,node = map(int,input().split())
    visited[row-1][node-1] = 1
if check():
    print(0)
else:
    for limit_insert_rows in range(1,4):
        dfs(0,0,0,limit_insert_rows)
        if result != float('inf'):
            print(result)
            break
    else:
        print(-1)