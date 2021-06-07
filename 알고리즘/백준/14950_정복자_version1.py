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


conquer = -1
pay_list = [[INF for _ in range(N+1)] for _ in range(2)]
pay_list[0][1] = 0
visted = [False]*(N+1)
cur_pay,cur_node = 0,1
result = 0
total_city = set(range(1,N+1))
while conquer<N-1:
    if visted[cur_node]:
        continue
    visted[cur_node] = True
    result += cur_pay
    total_city.remove(cur_node)
    conquer += 1
    idx = conquer%2
    if conquer > 0:
        prev_idx = (conquer+1)%2
        for city_num in total_city:
            pay_list[idx][city_num] = pay_list[prev_idx][city_num]+T
    
    min_idx = -1
    min_pay = INF
    for next_node in graph[cur_node]:
        temp_pay = graph[cur_node][next_node] + conquer*T
        if pay_list[idx][next_node] > temp_pay:
            pay_list[idx][next_node] = temp_pay

    for city_num in total_city:
        if min_pay > pay_list[idx][city_num]:
            min_pay = pay_list[idx][city_num]
            min_idx = city_num
    cur_pay,cur_node = min_pay,min_idx


print(result)
