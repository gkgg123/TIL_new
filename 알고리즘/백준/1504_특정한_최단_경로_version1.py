import sys
import heapq
def distra(start,ind):
    distance[ind][start] = 0
    node_list = []
    heapq.heappush(node_list,(0,start))
    while node_list:
        dis,node = heapq.heappop(node_list)
        if dis > distance[ind][node]:
            continue
        for next_node in graph[node]:
            if distance[ind][next_node] > dis + graph[node][next_node]:
                distance[ind][next_node] = dis + graph[node][next_node]
                heapq.heappush(node_list,(distance[ind][next_node],next_node))
input = sys.stdin.readline

N, E = map(int,input().split())
graph = [{} for i in range(N+1)]

for _ in range(E):
    A,B,C = map(int,input().split())
    graph[A][B] = C
    graph[B][A] = C

ess = list(map(int,input().split()))

INF = float('inf')
distance = [[INF]*(N+1) for _ in range(3)]

distra(1,0)
distra(N,1)
distra(ess[0],2)

a = distance[0][ess[0]] + distance[1][ess[1]] + distance[2][ess[1]]

b = distance[0][ess[1]] + distance[1][ess[0]] + distance[2][ess[1]]
result = min(a,b)
if result == INF:
    print(-1)
else:
    print(result)
