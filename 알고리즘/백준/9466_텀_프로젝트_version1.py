# # # 9466 텀 프로젝트
import sys
sys.setrecursionlimit(100000)



def dfs(node):
    global result
    visited[node] = False
    total.append(node)
    next_node = graph[node]
    if not visited[next_node]:
        if next_node in total:
            find_index = total.index(next_node)
    
            result +=total[find_index:]
        return
    else:
        dfs(next_node)


for _ in range(int(input())):
    N = int(input())
    graph = [0]+list(map(int,sys.stdin.readline().split()))
    visited = [True] *(N+1)
    result = []
    for ind in range(1,N+1):
        if visited[ind]:
            total = []
            dfs(ind)
    print(N-len(result))
