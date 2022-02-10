import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

H,W = map(int,input().split())

arr = []
lazer = []
for x in range(W):
    temp = input()
    for y in range(H):
        if temp[y] == 'C':
            lazer.append((x,y))
    arr.append(temp)

dx = [-1,0,1,0]
dy = [0,1,0,-1]

start_node,end_node = lazer

INF = float('inf')
visited = [[[INF for _ in range(4)] for _ in range(H)] for _ in range(W)]
node_list = []

for i in range(4):
    node_list.append((0,*start_node,i))
    visited[start_node[0]][start_node[1]][i] = 0


while node_list:
    dis,x,y,d = heapq.heappop(node_list)
    if visited[x][y][i] < dis:
        continue
    if (x,y) == end_node:
        print(dis)
        break
    for idx,i in enumerate([d,(d+1)%4,(d-1)%4]):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<W and 0<=ny<H:
            if arr[nx][ny] == '*':
                continue
            if visited[nx][ny][i] > dis + int(bool(idx)):
                visited[nx][ny][i] = dis + int(bool(idx))
                heapq.heappush(node_list,(visited[nx][ny][i],nx,ny,i))

