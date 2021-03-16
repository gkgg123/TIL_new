def solution(n, computers):
    answer = 0
    visited = [0]*(n+1)
    def dfs(node,cnt):
        nonlocal computers,visited
        for next_node,val in enumerate(computers[node-1]):
            if val and not visited[next_node+1]:
                visited[next_node+1] = cnt
                dfs(next_node+1,cnt)
    cnt = 1
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = cnt
            dfs(i,cnt)
            cnt += 1
    answer = max(visited)
    return answer

solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])