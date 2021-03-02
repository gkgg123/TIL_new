import heapq

def solution(n, s, a, b, fares):
    answer = float('inf')
    INF = float('inf')
    graph = [{} for i in range(n+1)]
    for start,end,fee in fares:
        graph[start][end] = fee
        graph[end][start] = fee
    Fee_list = [[INF]*(n+1) for _ in range(3)]
    def distra(start,idx):
        nonlocal graph,n,Fee_list
        node_list = []
        heapq.heappush(node_list,(0,start))
        Fee_list[idx][start] = 0 
        while node_list:
            fee,node = heapq.heappop(node_list)
            if fee > Fee_list[idx][node]:
                continue
            for next_node in graph[node]:
                temp_fee = fee + graph[node][next_node]
                if Fee_list[idx][next_node]> temp_fee:
                    Fee_list[idx][next_node] = temp_fee
                    heapq.heappush(node_list,(temp_fee,next_node)) 
    distra(s,0)
    distra(a,1)
    distra(b,2)
    for mid in range(1,n+1):
        temp = Fee_list[0][mid] + Fee_list[1][mid] + Fee_list[2][mid]
        if answer > temp:
            answer = temp
    return answer


solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])