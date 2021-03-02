import heapq


def solution(n, s, a, b, fares):
    answer = float('inf')
    INF = float('inf')
    graph = [[INF if x!=y else 0 for x in range(n+1)] for y in range(n+1)]
    for start,end,fee in fares:
        graph[start][end] = fee
        graph[end][start] = fee

    for mid in range(1,n+1):
        for start in range(1,n+1):
            for end in range(1,n+1):
                if graph[start][end] > graph[start][mid] + graph[mid][end]:
                    graph[start][end] = graph[start][mid] + graph[mid][end] 
        
    for k in range(1,n+1):
        answer = min(answer,graph[s][k]+graph[k][a]+graph[k][b])
    return answer
