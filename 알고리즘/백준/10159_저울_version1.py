import sys

input = sys.stdin.readline
N = int(input())
M = int(input())

graph = [[0 for _ in range(N+1)] for i in range(N+1)]
visited = [[True for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x][y] = -1
    visited[x][y] = False
    visited[y][x] = False



for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            if start == end:
                continue
            if graph[start][end] > graph[start][mid] + graph[mid][end] and graph[start][mid] and graph[mid][end]:
                graph[start][end] = graph[start][mid] + graph[mid][end]

result = []


for start in range(1,N+1):
    cnt = 0
    for end in range(1,N+1):
        if start == end:
            continue
        else:
            if graph[start][end] == 0 and graph[end][start] == 0:
                cnt += 1
    result.append(cnt)

for row in result:
    sys.stdout.write(str(row)+'\n')