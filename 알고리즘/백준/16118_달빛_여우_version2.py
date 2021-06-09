import sys
import heapq
input = sys.stdin.readline
def dijkstra_fox():
    distance = [INF for _ in range(N+1)]

    distance[1] = 0
    node_list = []
    heapq.heappush(node_list,(0,1))
    cnt = N-1
    while node_list and cnt:
        dis,cur_node = heapq.heappop(node_list)
        if distance[cur_node] < dis:
            continue

        for next_node,next_val in graph[cur_node]:
            
            if distance[next_node] > next_val + dis:
                distance[next_node] = next_val + dis
                heapq.heappush(node_list,(distance[next_node],next_node))
        cnt -= 1
    return distance


def dijkstra_wolf():
    distance = [[INF for _ in range(N+1)] for _ in range(2)]
    distance[1][1] = 0
    node_list = []
    heapq.heappush(node_list,(0,1,1))
    cnt = 2*N-1
    while node_list and cnt:
        dis,cur_node,turn = heapq.heappop(node_list)
        turn = turn%2
        next_turn = (turn+1)%2
        if distance[turn][cur_node] < dis:
            continue
        for next_node,next_val in graph[cur_node]:
            if turn:
                next_distance = dis + next_val//2
            else:
                next_distance = dis + next_val*2
            
            if distance[next_turn][next_node] > next_distance:
                distance[next_turn][next_node] = next_distance
                heapq.heappush(node_list,(next_distance,next_node,next_turn))
        cnt -= 1
    return distance
N,M = map(int,input().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    x,y,d = map(int,input().split())
    graph[x].append([y,d*2]) 
    graph[y].append([x,d*2])

INF= float('inf')

distance_fox = dijkstra_fox()
distance_wolf = dijkstra_wolf()
result = 0
for i in range(2,N+1):
    if distance_fox[i] < distance_wolf[0][i] and distance_fox[i] < distance_wolf[1][i]:
        result += 1

print(result)
