import math
import sys


def dfs(node):
    stack = [(node,0,0)]
    visited = [True]*(N+1)
    distance = 0
    max_node = -1
    min_time = float('inf')
    visited[node] = False
    while stack:
        node,dis,time = stack.pop()
        if dis > distance:
            distance = dis
            max_node = node
            min_time = time
        elif dis == distance and min_time > time:
            max_node = node
            min_time = time

        for next_node in graph[node]:
            if visited[next_node]:
                new_dis = dis + 1
                new_time = time + graph[node][next_node]
                visited[next_node] = False
                stack.append((next_node,new_dis,new_time))

    return [max_node,distance,min_time]

 

input = sys.stdin.readline

N,T = map(int,input().split())


graph = [{} for _ in range(N+1)]


for _ in range(N-1):
    x,y,time = map(int,input().split())
    graph[x][y] = time
    graph[y][x] = time

far_node_info = dfs(1)

result = dfs(far_node_info[0])


print(math.ceil(result[2]/T))


