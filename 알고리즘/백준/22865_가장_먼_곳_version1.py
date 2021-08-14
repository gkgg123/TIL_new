import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
person = list(map(int,input().split()))


graph = [{} for _ in range(N+1)]

for _ in range(int(input())):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x].get(y,float('inf')),pay)
    graph[y][x] = min(graph[y].get(x,float('inf')),pay)




result = float('inf')
INF = float('inf')
distance_list = [INF for _ in range(N+1)]
node_list = []



for index in range(3):
    person_city = person[index]

    heapq.heappush(node_list,(0,person_city))
    distance_list[person_city] = 0


home_set = list(set(range(1,N+1)) - set(person))
home_set.sort()
while node_list:
    cur_dis,  cur_node = heapq.heappop(node_list)

    if distance_list[cur_node] < cur_dis:
        continue

    for next_node in graph[cur_node]:
        if distance_list[next_node] > cur_dis + graph[cur_node][next_node]:
            distance_list[next_node] = cur_dis + graph[cur_node][next_node]
            heapq.heappush(node_list,(distance_list[next_node] , next_node))




result = -1
answer = 0
for home in home_set:
    if distance_list[home] > answer:
        result = home
        answer = distance_list[home]

print(result)