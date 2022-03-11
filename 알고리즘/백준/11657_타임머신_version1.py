import sys

def input():
    return sys.stdin.readline().rstrip()


def belman_ford():
    INF = float('inf')
    time_list = [INF for _ in range(N+1)]
    time_list[1] = 0
    for idx in range(N+2):
        for node in range(1,N+1):
            for next_node in graph[node]:
                next_time = graph[node][next_node]
                if time_list[next_node] > time_list[node] + next_time:
                    time_list[next_node] = time_list[node] + next_time
                    if idx>= N:
                        return [-1]
    return  [-1 if val == INF else val for val in time_list[2:]]

N,M = map(int,input().split())
graph = [{} for _ in range(N+1)]

for _ in range(M):
    a,b,pay = map(int,input().split())
    graph[a][b] = min(graph[a].get(b,float('inf')),pay)

for row in belman_ford():
    print(row)

