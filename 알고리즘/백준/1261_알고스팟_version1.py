import heapq
import sys
input = sys.stdin.readline
N,M = map(int,input().split())

arr = [list(map(int,list(input().strip()))) for _ in range(M)]

node_list = []
heapq.heappush(node_list,(0,0,0))
INF = float('inf')
dp = [[INF]*N for _ in range(M)]
dx = [-1,1,0,0]
dy = [0,0,1,-1]
dp[0][0] = 0
while node_list:
    dis,x,y = heapq.heappop(node_list)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<M and 0<=ny<N:
            if dp[nx][ny] > dp[x][y] + arr[nx][ny]:
                dp[nx][ny] = dp[x][y] + arr[nx][ny]
                heapq.heappush(node_list,(dp[nx][ny],nx,ny))

print(dp[M-1][N-1])