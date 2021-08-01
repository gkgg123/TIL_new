import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

def solution():
    priority_que = []
    for num in range(1,N+1):
        if not indegree[num]:
            priority_que.append(num)
    heapq.heapify(priority_que)

    result = []
    while priority_que:
        num = heapq.heappop(priority_que)
        result.append(num)
        for next_num in graph[num]:
            indegree[next_num] -= 1
            if not indegree[next_num]:
                heapq.heappush(priority_que,next_num)
    return result

N,M = map(int,input().split())

graph = [ [] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y)
    indegree[y] += 1

print(*solution())