import sys

def input():
    return sys.stdin.readline().rstrip()

def innerCircle(a,b):
    x1,y1,r1 = a
    x2,y2,r2 = b
    return (x1-x2)**2 + (y1-y2)**2 < (r1-r2)**2


def dfs(node):
    distance_list = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[node] = True
    stack = [(node,0)]
    while stack:
        node,distance = stack.pop()
        distance_list[node] = distance
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node,distance+1))
    return distance_list

N = int(input())

circle_list = [(0,0,2000000)]
for _ in range(N):
    x,y,r = map(int,input().split())
    circle_list.append((x,y,r))

circle_list.sort(key = lambda x : x[2])
graph = [[] for _ in range(N+1)]
for i in range(N):
    for j in range(i+1,N+1):
        if innerCircle(circle_list[i],circle_list[j]):
            graph[i].append(j)
            graph[j].append(i)
            break


distance1 = dfs(N)
distance2 = dfs(distance1.index(max(distance1)))

print(max(distance2))