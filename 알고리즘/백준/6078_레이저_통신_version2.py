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
visited = [[INF for _ in range(H)] for _ in range(W)]
node_list = []

node_list.append((0,*start_node))
visited[start_node[0]][start_node[1]] = 0


while node_list:
    dis,x,y= heapq.heappop(node_list)
    if visited[x][y] < dis:
        continue
    if (x,y) == end_node:
        print(dis-1)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        while 0<=nx<W and 0<=ny<H:
            
            if arr[nx][ny] == '*':
                break

            if visited[nx][ny] < dis + 1:
                break
            visited[nx][ny] = dis + 1
            heapq.heappush(node_list,(visited[nx][ny],nx,ny))
            nx += dx[i]
            ny += dy[i]


