import sys

def input():
    return sys.stdin.readline().rstrip()

N,M = map(int,input().split())

INF = float('inf')
dis = [[INF if i != j else 0 for j in range(N)] for i in range(N)]
next_module = [[0 for _ in range(N)] for _ in range(N)]


for _ in range(M):
    x,y,d = map(int,input().split())
    x-= 1;y-=1
    dis[x][y] = min(dis[x][y],d)
    dis[y][x] = min(dis[y][x],d)
    next_module[y][x] = x+1
    next_module[x][y] = y+1

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if dis[start][end] > dis[start][mid] + dis[mid][end]:
                dis[start][end] = dis[start][mid] + dis[mid][end]
                next_module[start][end] = next_module[start][mid]


for x in range(N):
    for y in range(N):
        if x == y:
            print('-',end=' ')
        else:
            print(next_module[x][y],end=' ')
    print()