import sys

input = sys.stdin.readline
def dfs(node,flag,*args):
    stack = [(node,0)]
    distance_list = [0 for _ in range(N+1)]
    visited = [False for _ in range(N+1)]
    visited[node] = True
    if not flag:
        visited[args[0]] = True
    while stack:
        node,distance = stack.pop()
        distance_list[node] = distance

        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                stack.append((next_node,distance+graph[node][next_node]))
    
    temp = []

    for i in range(1,N+1):
        temp.append((distance_list[i],i))
    temp.sort(key=lambda x :-x[0])
    if flag:
        return_value = temp[0][1]
    else:
        return_value = temp[0][0]
    return return_value


N = int(input())
graph = [{} for _ in range(N+1)]
for _ in range(N-1):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    graph[y][x] = pay

first_point = dfs(1,True)
second_point = dfs(first_point,True)

first_value = dfs(first_point,False,second_point)
second_value = dfs(second_point,False,first_point)

print(max(first_value,second_value))