import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())


dire = {
    "U": [-1,0],
    "L": [0,-1],
    "R" : [0, 1],
    'D': [1,0]
}
arr = [list(input()) for _ in range(N)]
visited = [[-1 for _ in range(M)] for _ in range(N)]

result = 0
for x in range(N):
    for y in range(M):
        if visited[x][y] != -1:
            continue

        point = x*M+y
        nx,ny = x,y
        while visited[nx][ny] == -1:
            visited[nx][ny] = point
            dx,dy = dire[arr[nx][ny]]
            nx = nx + dx
            ny = ny + dy
        if visited[nx][ny] == point:
            result += 1
print(result)