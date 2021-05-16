import sys

sys.setrecursionlimit(10000)
def roll(x,y,vis,cnt,roll_cnt):
    global result,total_cnt
    if total_cnt == cnt:
        result = min(result,roll_cnt)
        return
    if roll_cnt > result:
        return
    vis[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    for i in range(4):
        move = 1
        nx = x + dx[i]*move
        ny = y + dy[i]*move
        while 0<=nx<N and 0<=ny<M and vis[nx][ny] == False:
            nx = nx + dx[i]
            ny = ny + dy[i]
            move += 1
        if move>1:
            for m in range(1,move):
                nx = x + dx[i]*m
                ny = y + dy[i]*m
                vis[nx][ny] = True
            
            roll(nx,ny,vis,cnt+(move-1),roll_cnt+1)

            for m in range(1,move):
                nx = x + dx[i]*m
                ny = y + dy[i]*m
                vis[nx][ny] = False




tc = 1
while True:
    try:
        N,M = map(int,input().split())
        arr = []
        total_cnt = N*M
        visited = [[False]*M for _ in range(N)]
        for x in range(N):
            temp = list(input())
            for y in range(M):
                if temp[y] == '*':
                    visited[x][y] = True
                    total_cnt -= 1
            
            arr.append(temp)

        result = float('inf')
        for x in range(N):
            for y in range(M):
                if arr[x][y] == '.':
                    copy_visited = [row[:] for row in visited]
                    roll(x,y,copy_visited,1,0)

        if result == float('inf'):
            result = -1
        print(f'Case {tc}: {result}')
        tc += 1
    except:
        break