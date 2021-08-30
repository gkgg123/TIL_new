import sys
def input():
    return sys.stdin.readline().rstrip()
N,M,R = map(int,input().split())
arr = [0] + list(map(int,input().split()))

graph = [{} for _ in range(N+1)]


INF = float('inf')
distance = [[0 if i == j else INF for j in range(N+1)] for i in range(N+1)]
for _ in range(R):
    x,y,pay = map(int,input().split())
    graph[x][y] = min(graph[x].get(y,float('inf')), pay)
    graph[y][x] = min(graph[y].get(x, float('inf')),pay)
    distance[x][y] = min(distance[x][y],pay)
    distance[y][x] = min(distance[y][x],pay)

value = [0 for _ in range(N+1)]
for mid in range(1,N+1):
    for start in range(1,N+1):
        for end in range(1,N+1):
            if distance[start][end] > distance[start][mid] + distance[mid][end]:
                distance[start][end] =  distance[start][mid] + distance[mid][end]


result = 0
for node in range(1,N+1):
    temp = 0
    for next_node in range(1,N+1):
        if distance[node][next_node] <= M:
            temp += arr[next_node]
    if temp > result:
        result = temp
print(result)