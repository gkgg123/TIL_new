import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def bfs():
    visited = [-1 for _ in range(N+1)]
    for st in range(1,N+1):
        if visited[st] == -1:
            queue = deque()
            queue.append(st)
            visited[st] = 0
            while queue:
                x = queue.popleft()

                for next_x in graph[x]:
                    if visited[next_x] == -1:
                        visited[next_x] = (visited[x]+1)%2
                        queue.append(next_x)
                    elif visited[next_x] == visited[x]:
                        return 'NO'
    return 'YES'
T = int(input())

for i in range(T):
    N,E = map(int,input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(E):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    print(bfs())


    