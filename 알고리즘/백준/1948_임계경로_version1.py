import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def solution(S,E):
    distance_list = [0 for _ in range(N+1)]
    node_list = deque()
    distance_list[S] = 0
    node_list.append(S)
    while node_list:
        cur_node = node_list.popleft()

        for next_node in graph[cur_node]:
            if distance_list[next_node] < distance_list[cur_node] + graph[cur_node][next_node]:
                distance_list[next_node] = distance_list[cur_node] + graph[cur_node][next_node]
            indegree[next_node] -= 1
            if not indegree[next_node]:
                node_list.append(next_node)


    stack = [(E,distance_list[E])]
    path_set = set()
    visited = set()
    while stack:
        node,dis = stack.pop()
        if node in visited:continue
        visited.add(node)
        for prev_node in parents[node]:
            if (prev_node,node) not in path_set:
                if distance_list[prev_node] + graph[prev_node][node] == dis:
                    path_set.add((prev_node,node))
                    stack.append((prev_node,distance_list[prev_node]))
    print(distance_list[E])
    print(len(path_set))


N = int(input())

graph = [{} for _ in range(N+1)]
parents = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
for _ in range(int(input())):
    x,y,pay = map(int,input().split())
    graph[x][y] = pay
    parents[y].append(x)
    indegree[y] += 1
S,E = map(int,input().split())
solution(S,E)