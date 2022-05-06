import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def outOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False


N,M,K = map(int,input().split())


arr = [list(input()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]
cnt = [[[0,0,0,0] for _ in range(M)] for _ in range(N)]
x1,y1,x2,y2 = map(lambda x : x-1,map(int,input().split()))

queue = deque()
queue.append((x1,y1,0))
dx = [-1,0,1,0]
dy = [0,-1,0,1]
visited[x1][y1] = 0
flag = True
while queue:
    x,y,t = queue.popleft()

    for i in range(4):
        found_L = cnt[x][y][i]+1
        min_L = K
        for l in range(cnt[x][y][i]+1,K+1):
            nx = x + dx[i]*l
            ny = y + dy[i]*l
            found_L = l
            if not outOfBound(nx,ny) or arr[nx][ny] == '#' or (visited[nx][ny] != -1 and visited[nx][ny]<t+1):
                found_L -= 1
                break
            elif visited[nx][ny] == -1:
                min_L = min(l,min_L)
        for l in range(min_L,found_L+1):
            nx = x + dx[i]*l
            ny = y + dy[i]*l
            cnt[nx][ny][i] = max(cnt[nx][ny][i],found_L-l)
            if visited[nx][ny] == -1:
                visited[nx][ny] = t+1
                queue.append((nx,ny,t+1))
                if (nx,ny) == (x2,y2):
                    print(t+1)
                    exit()
if flag:
    print(-1)