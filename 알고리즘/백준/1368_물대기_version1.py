import sys
import heapq
input = sys.stdin.readline



N = int(input())
node_list = []
pay_list = []

for i in range(N):
    pay = int(input())
    heapq.heappush(node_list,(pay,i))
    pay_list.append(pay)


connect_list = [list(map(int,input().split())) for _ in range(N)]

result = 0
visited = [False]*N
while node_list:
    pay,node = heapq.heappop(node_list)
    if visited[node]:
        continue
    visited[node] = True
    result += pay

    for next_node in range(N):
        if next_node != node:
            if pay_list[next_node] > connect_list[node][next_node]:
                pay_list[next_node] = connect_list[node][next_node]
                heapq.heappush(node_list,(pay_list[next_node],next_node))


print(result)