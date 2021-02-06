for _ in range(int(input())):
    N = int(input())
    graph = list(map(int,input().split()))
    visited = [0]*N
    cnt = 0
    for current_node in range(N):
        if not visited[current_node]:
            next_node = current_node
            while visited[next_node] == 0:
                visited[next_node] = 1
                next_node = graph[next_node] - 1
            cycle_index = current_node
            while cycle_index != next_node:
                cnt += 1
                cycle_index = graph[cycle_index] - 1

    print(cnt)

            