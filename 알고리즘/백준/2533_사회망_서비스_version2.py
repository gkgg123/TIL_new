import sys

def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(1000001)
def dfs(node):
    global answer
    visited[node] = True
    if len(graph[node]) == 1 and node != 0:
        answer -= 1
        return False
    result = True
    for child in graph[node]:
        if not visited[child]:
            visited[child] = True
            result &= dfs(child)
    if result:
        answer -= 1
        return False
    return True
N = int(input())
graph = [[] for _ in range(N)]
visited = [False for _ in range(N)]
answer = N
for _ in range(N-1):
    x,y = map(int,input().split())
    x -= 1
    y -= 1
    graph[x].append(y)
    graph[y].append(x)

dfs(0)
print(answer)