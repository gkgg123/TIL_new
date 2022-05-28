import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def distance(x1,y1,x2,y2):
    return ((y1-y2)**2 + (x1-x2)**2)**0.5

N = int(input())
stars = []
graph = [{} for _ in range(N)]
for idx in range(N):
    x,y = map(float,input().split())
    for prev_star in range(idx):
        px,py = stars[prev_star]
        dis = distance(px,py,x,y)
        graph[idx][prev_star] = dis
        graph[prev_star][idx] = dis
    stars.append((x,y))

INF = float('inf')

distance_list = [INF for _ in range(N)]
distance_list[0] = 0
node_list = []
answer= 0
visited = [True for _ in range(N)]
heapq.heappush(node_list,(0,0))
while node_list:
    cur_dis,node = heapq.heappop(node_list)
    if not visited[node]:
        continue
    visited[node] = False
    answer += cur_dis
    for next_node in graph[node]:
        if distance_list[next_node] > graph[node][next_node]:
            distance_list[next_node] = graph[node][next_node]
            heapq.heappush(node_list,(distance_list[next_node],next_node))

print(f'{answer:.2f}')