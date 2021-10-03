import sys
import heapq
sys.setrecursionlimit(100000)
def input():
    return sys.stdin.readline().rstrip()

def dfs(node):
    global flag
    visited_node[node] = True
    if node == goal:
        flag = True
        return [node]
    if flag:
        return []
    temp = []
    for next_node in graph[node]:
        if not visited_node[next_node]:
            temp.extend(dfs(next_node))
    if temp:
        return [node,*temp]
    return []

N = int(input())

circle_list = []
for i in range(1,N+1):
    num,x,r = map(int,input().split())
    circle_list.append((x-r,num))
    circle_list.append((x+r,-num))



heapq.heapify(circle_list)
graph = [[] for _ in range(N+1)]
stack = [0]

while circle_list:
    position, ind = heapq.heappop(circle_list)
    if ind < 0:
        stack.pop()
    else:
        graph[stack[-1]].append(ind)
        graph[ind].append(stack[-1])
        stack.append(ind)


flag = False
start,goal = map(int,input().split())
visited_node = [False for _ in range(N+1)]
result = dfs(start)
print(len(result))
print(*result)