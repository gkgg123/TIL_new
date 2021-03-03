import sys
input = sys.stdin.readline




V,E = map(int,input().split())
graph = [{} for _ in range(V+1)]

for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    graph[B][A] = C
INF = float('inf')
visited = [False]*(V+1)
distance = [INF]*(V+1)
distance[1] = 0

node_list = [(1,0)]
cnt = 1
result = 0
while cnt <V:
    node, dis = node_list.pop()
    current_min_dis = INF
    current_min_node = -1
    visited[node] = True
    for next_node in graph[node]:
        if distance[next_node] > graph[node][next_node]:
            distance[next_node] =  graph[node][next_node]

    for ind in range(1,V+1):
        if current_min_dis > distance[ind] and not visited[ind]:
            current_min_node = ind
            current_min_dis = distance[ind]
    node_list.append((current_min_node,current_min_dis))
    result += current_min_dis
    cnt += 1

print(result)