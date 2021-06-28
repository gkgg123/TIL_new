import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


def bfs(queue):
    dx = [-1,0,1,-1,1,-1,0,1]
    dy = [-1,-1,-1,0,0,1,1,1]
    while queue:
        x,y,cnt = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0<=nx<N and 0<=ny<M):continue
            if arr[nx][ny]:
                arr[nx][ny] -= 1
                if not arr[nx][ny]:
                    queue.append((nx,ny,cnt+1))

    return cnt

N,M = map(int,input().split())


arr = [list(input()) for _ in range(N)]


sand_deque = deque()
for x in range(N):
    for y in range(M):
        if arr[x][y].isdigit():
            arr[x][y] = int(arr[x][y])
        else:
            arr[x][y] = 0
            sand_deque.append((x,y,0))



print(bfs(sand_deque))
