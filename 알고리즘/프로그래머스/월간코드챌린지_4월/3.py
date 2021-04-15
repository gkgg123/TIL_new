import sys

sys.setrecursionlimit(300000)

def solution(a, edges):
    answer = 0
    graph = [[] for _ in range(len(a))]
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])
    if sum(a) != 0:
        answer = -1
    else:
        visited = [False] * len(a)
        def dfs(node,parent):
            nonlocal a
            visited[node] = True
            child_node = []

            for connect_node in graph[node]:
                if not visited[connect_node]:
                    child_node.append(connect_node)
            answer = 0
            if child_node:
                for child in child_node:
                    answer += dfs(child,node)
                if node != parent:
                    answer += abs(a[node])
                    a[parent] = a[parent] + a[node]
                    a[node] = 0

            else:
                answer += abs(a[node])
                a[parent] = a[parent] +a[node]
                a[node] = 0
            return answer




        if any(a):
            answer = dfs(0,0)

    return answer


solution([0,1,-1],[[0,1],[1,2]])