import heapq
import sys

def dijkstra(S,E,TERM):
    INF = float('inf')
    distance_list = [INF]*(N+1)
    distance_list[S] = TERM
    node_list = []
    heapq.heappush(node_list,(TERM,S))

    while node_list:
        cur_time,cur_node = heapq.heappop(node_list)

        for next_node in graph[cur_node]:
            if time_spend_list.get((cur_node,next_node)) and time_spend_list[(cur_node,next_node)][0]<=cur_time<=time_spend_list[(cur_node,next_node)][1]:
                spend_time = time_spend_list[(cur_node,next_node)][1] + graph[cur_node][next_node]
            else:
                spend_time = cur_time + graph[cur_node][next_node]
            
            if distance_list[next_node] > spend_time:
                distance_list[next_node] = spend_time
                heapq.heappush(node_list,(spend_time,next_node))

    return distance_list


input = sys.stdin.readline

N,M = map(int,input().split())

start_point,end_point,king_term,G = map(int,input().split())

king_visit_list = list(map(int,input().split()))


graph = [{} for _ in range(N+1)]

for _ in range(M):
    x,y,times = map(int,input().split())

    graph[x][y] = min(graph[x].get(y,float('inf')),times)
    graph[y][x] = min(graph[y].get(x,float('inf')),times)



time_spend_list = {}

king_time = 0
for ind in range(G-1):
    start,ends = king_visit_list[ind],king_visit_list[ind+1]
    time_spend_list[(start,ends)] = (king_time,king_time+graph[start][ends])
    time_spend_list[(ends,start)] = (king_time,king_time+graph[start][ends])
    king_time += graph[start][ends]


result = dijkstra(start_point,end_point,king_term)


print(result[end_point]-king_term)