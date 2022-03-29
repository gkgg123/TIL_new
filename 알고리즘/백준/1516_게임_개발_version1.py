import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()


N = int(input())


indegree = [0 for _ in range(N+1)]

spend_time = [0 for _ in range(N+1)]

ordeed = [[] for _ in range(N+1)]

for number in range(1,N+1):
    time, *preceding,_ = map(int,input().split())
    for pa in preceding:
        ordeed[pa].append(number)
    indegree[number] += len(preceding)
    spend_time[number] = time

queue = []
for number in range(1,N+1):
    if not indegree[number]:
        heapq.heappush(queue,(spend_time[number],number))

result = [0 for _ in range(N+1)]
while queue:
    complete_time, node_number = heapq.heappop(queue)
    result[node_number] = complete_time
    for next_node in ordeed[node_number]:
        indegree[next_node] -= 1
        if not indegree[next_node]:
            heapq.heappush(queue,(spend_time[next_node] + complete_time,next_node))


for number in range(1,N+1):
    print(result[number])