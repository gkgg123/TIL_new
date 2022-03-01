import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

goorm = [(N-1,0),(N-1,1),(N-2,0),(N-2,1)]


bucket = [list(map(int,input().split())) for _ in range(N)]
visited = [[True for _ in range(N)] for _ in range(N)]
# 1,3,5,7
dx = [0,-1,-1,-1,0,1,1,1]
dy = [-1,-1,0,1,1,1,0,-1]
for _ in range(M):
    dire, size = map(int,input().split())
    dire -= 1
    next_goorm = []

    for x,y in goorm:
        nx = (x + dx[dire]*size)%N
        ny = (y + dy[dire]*size)%N
        next_goorm.append([nx,ny])
        bucket[nx][ny] += 1
        visited[nx][ny] = False

    for x,y in next_goorm:
        for i in range(1,8,2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N and bucket[nx][ny]:
                bucket[x][y] += 1
    goorm = []

    for x in range(N):
        for y in range(N):
            if bucket[x][y] >= 2 and visited[x][y]:
                goorm.append([x,y])
                bucket[x][y] -= 2
            visited[x][y] = True



result = sum(list(map(lambda x : sum(x),bucket)))
print(result)