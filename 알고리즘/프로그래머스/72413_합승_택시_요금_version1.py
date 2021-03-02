import heapq


def solution(n, s, a, b, fares):
    answer = float('inf')
    total_node = set(range(1,n+1))
    graph = [{} for i in range(n+1)]
    for start,end,fee in fares:
        graph[start][end] = fee
        graph[end][start] = fee
    def distra(start,end):
        nonlocal graph,n
        node_list = []
        heapq.heappush(node_list,(0,start))
        INF = float('inf')
        Fee_list = [INF]*(n+1)
        Fee_list[start] = 0
        while node_list:
            fee,node = heapq.heappop(node_list)
            if fee > Fee_list[node]:
                continue
            if node == end:
                return fee
            for next_node in graph[node]:
                temp_fee = fee + graph[node][next_node]
                if Fee_list[next_node]> temp_fee:
                    Fee_list[next_node] = temp_fee
                    heapq.heappush(node_list,(temp_fee,next_node)) 
        return INF
        
    for k in total_node:
        answer = min(answer,distra(s,k)+distra(k,a)+distra(k,b))
    return answer

solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])