import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


N,M,K = map(int,input().split())


arr = [list(map(int, list(input()))) for _ in range(N)]


INF = float('inf')
visited = [[[INF for _ in range(K+1)] for _ in range(M)] for _ in range(N)]
'''
7 4 2
0101
1100
1110
0000
0111
0111
0100
'''

queue = deque()

queue.append((0,0,0,K))
visited[0][0][K] = 0
flag = True
dx = [-1,1,0,0]
dy = [0,0,-1,1]
while queue:
    x,y,dis,cnt = queue.popleft()
    if x == N-1 and y ==M-1:
        print(dis+1)
        flag = False
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<N and 0<=ny<M:
            if arr[nx][ny] and cnt>0 and visited[nx][ny][cnt-1] == INF:
                visited[nx][ny][cnt-1] = dis + 1
                queue.append((nx,ny,dis+1,cnt-1))
            elif not arr[nx][ny] and visited[nx][ny][cnt] == INF:
                visited[nx][ny][cnt] = dis + 1
                queue.append((nx,ny,dis+1,cnt))

if flag:
    print(-1)