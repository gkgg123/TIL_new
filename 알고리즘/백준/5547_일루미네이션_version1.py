import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()


M,N = map(int,input().split())


arr = [[0 for _ in range(M+2)]]

for _ in range(N):
    temp = list(map(int,input().split()))
    arr.append([0]+temp+[0])

arr.append([0 for _ in range(M+2)])

dx = [-1,-1,0,0,1,1]
dy = [[-1,0,-1,1,-1,0],[0,1,-1,1,0,1]]
WN = N+2
WM = M+2
queue = deque()
queue.append((0,0))
arr[0][0] = -1
while queue:
    cx,cy = queue.popleft()
    for i in range(6):
        nx = cx + dx[i]
        ny = cy + dy[cx%2][i]

        if 0<=nx<WN and 0<=ny<WM:
            if not arr[nx][ny]:
                arr[nx][ny] = -1
                queue.append((nx,ny))


visited = [[False for _ in range(WM)] for _ in range(WN)]
answer = 0
for x in range(WN):
    for y in range(WM):
        if arr[x][y] == 1:
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[x%2][i]
                if 0<=nx<WN and 0<=ny<WM:
                    if arr[nx][ny] == -1:
                        answer += 1

print(answer)
