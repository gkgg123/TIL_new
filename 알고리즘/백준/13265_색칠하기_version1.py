import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(node):
    queue = deque()
    queue.append((node,0))
    visit[node] = 0
    while queue:
        cur,color = queue.popleft()

        for next_node in graph[cur]:
            if visit[next_node] == -1:
                visit[next_node] = (color+1)%2
                queue.append((next_node,visit[next_node]))
            elif visit[next_node] == color:
                return False
    return True

T = int(input())

for _ in range(T):
    N,M = map(int,input().split())
    visit = [-1 for _ in range(N+1)]
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        x,y = map(int,input().split())
        graph[x].append(y)
        graph[y].append(x)
    answer = True
    for i in range(1,N+1):
        if visit[i] == -1:
            answer&=bfs(i)
    print('possible' if answer else 'impossible')