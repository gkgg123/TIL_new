import collections
dx = [-1,0,1,-1,1,-1,0,1]
dy = [-1,-1,-1,0,0,1,1,1]
N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
shark = collections.deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            shark.append((i,j,arr[i][j]))

while shark:
    x,y,dis = shark.popleft()
    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<= nx <N and 0<=ny<M:
            if not arr[nx][ny]:
                arr[nx][ny] = 1
                shark.append((nx,ny,dis+1))


print(dis-1)
