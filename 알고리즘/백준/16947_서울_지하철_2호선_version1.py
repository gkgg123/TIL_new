import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()

def cycle_check(node,parent):
    if visited[node]:
        return node
    else:
        visited[node] = True
        for next_node in graph[node]:
            if next_node == parent:continue
            return_node = cycle_check(next_node,node)
            if return_node > 0:
                cycle_check_node[node] = True
                if return_node == node:
                    return 0
                else:
                    return return_node
        cycle_check_node[node] = False
        return 0
def dfs(start):
    stack = [(start,0,0)]
    visited = [True for _ in range(N+1)]
    while stack:
        node,parent,dis = stack.pop()

        if cycle_check_node[node]:
            distance[start] = dis
            return
        visited[node] = False

        for next_node in graph[node]:
            if next_node == parent:continue
            if visited[next_node]:
                stack.append((next_node,node,dis+1))



N = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(N):
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)


visited = [False for _ in range(N+1)]
cycle_check_node = [False for _ in range(N+1)]
distance = [0 for _ in range(N+1)]

cycle_check(1,0)


for k in range(1,N+1):
    if not cycle_check_node[k]:
        dfs(k)


print(*distance[1:])