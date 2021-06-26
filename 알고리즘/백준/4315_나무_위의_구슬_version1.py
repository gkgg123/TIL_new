import sys
input = sys.stdin.readline
def dfs(node):
    global result 
    if not len(graph[node]):
        ball_cnt_list[parent_list[node]] += (ball_cnt_list[node] -1)
        result += abs(ball_cnt_list[node] - 1)
    else:
        for next_node in graph[node]:
            dfs(next_node) 
        if parent_list[node] != -1:
            ball_cnt_list[parent_list[node]] += ball_cnt_list[node] - 1
            result += abs(ball_cnt_list[node] - 1)



while True:
    N = int(input())

    if N == 0:
        break
    graph = [[] for _ in range(N+1)]
    parent_list = [-1 for _ in range(N+1)]
    ball_cnt_list = [0 for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(N):
        node_num,ball_cnt,*arg = map(int,input().split())
        if arg[0]>0:
            for child_node in arg[1:]:
                graph[node_num].append(child_node)
                parent_list[child_node] = node_num
                indegree[child_node] += 1
        ball_cnt_list[node_num] = ball_cnt

    result = 0
    for k in range(1,N+1):
        if indegree[k] == 0:
            dfs(k)
    print(result)