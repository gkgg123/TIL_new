import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def distance(p1,p2):
    return (p1[0] - p2[0])**2 + (p1[1]-p2[1])**2
N,W = map(int,input().split())
M = float(input())
M = M**2
position = []

for _ in range(N):
    x,y = map(int,input().split())
    position.append((x,y))
graph = [{} for _ in range(N)]

for ind1 in range(N-1):
    for ind2 in range(ind1+1,N):
        two_distance = distance(position[ind1],position[ind2])
        if two_distance <= M:
            graph[ind1][ind2] = two_distance**0.5
            graph[ind2][ind1] = two_distance**0.5
for _ in range(W):
    a,b = map(lambda x: x-1, map(int,input().split()))
    graph[a][b] = 0
    graph[b][a] = 0

INF = float('inf')
distance_list = [INF for _ in range(N)]
distance_list[0] = 0
node_list = []
node_list.append((0,0))

while node_list:
    cur_dis,cur_node = heapq.heappop(node_list)
    if cur_dis > distance_list[cur_node]:
        continue
    for next_node in graph[cur_node]:
        if distance_list[next_node] > cur_dis + graph[cur_node][next_node]:
            distance_list[next_node] = cur_dis + graph[cur_node][next_node]

            heapq.heappush(node_list,(distance_list[next_node],next_node))

print(int(distance_list[N-1]*1000))