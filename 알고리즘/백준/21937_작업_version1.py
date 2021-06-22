import sys
input = sys.stdin.readline
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[y].append(x)


start = int(input())
stack = [start]
cnt = 0
visited = [True for _ in range(N+1)]
visited[start] = False
while stack:
    x = stack.pop()

    for next_node in graph[x]:
        if visited[next_node]:
            visited[next_node] = False
            cnt += 1
            stack.append(next_node)

print(cnt)
