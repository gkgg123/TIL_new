import sys
import heapq
input = sys.stdin.readline


N,M,T = map(int,input().split())



graph = [{} for _ in range(N+1)]
INF = float('inf')
for _ in range(M):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x].get(y,INF),pay)
    graph[y][x] = min(graph[y].get(x,INF),pay)



pay_list =[INF for _ in range(N+1)]
node_list = []
visited = [False]*(N+1)
heapq.heappush(node_list,(0,1))
pay_list[1] = 0
result = 0
while node_list:
    cur_pay,cur_node = heapq.heappop(node_list)
    if pay_list[cur_node] < cur_pay or visited[cur_node]:
        continue
    visited[cur_node] = True
    result += cur_pay
    for next_node in graph[cur_node]:
        if pay_list[next_node] > graph[cur_node][next_node] and not visited[next_node]:
            pay_list[next_node] = graph[cur_node][next_node]
            heapq.heappush(node_list,(pay_list[next_node],next_node))


conquer_pay = (N-2)*(T+(N-2)*T)//2
result += conquer_pay
print(result)