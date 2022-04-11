import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    work_times = [0] + list(map(int,input().split()))
    graph = [[] for _ in range(N+1)]
    indegree = [0 for _ in range(N+1)]
    for _ in range(K):
        x,y = map(int,input().split())

        graph[x].append(y)
        indegree[y] += 1

    W = int(input())
    spend_time = [0 for _ in range(N+1)]
    queue = []
    for num in range(1,N+1):
        if not indegree[num]:
            spend_time[num] = work_times[num]
            heapq.heappush(queue,(spend_time[num],num))

    while queue:
        cur_time,idx = heapq.heappop(queue)
        if idx == W:
            print(cur_time)
            break

        for next_node in graph[idx]:
            indegree[next_node] -= 1
            if not indegree[next_node]:
                heapq.heappush(queue,(cur_time + work_times[next_node],next_node))


