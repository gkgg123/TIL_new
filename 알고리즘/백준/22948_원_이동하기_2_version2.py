from collections import deque
import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

circle_list = []
for i in range(1,N+1):
    num,x,r = map(int,input().split())
    circle_list.append((x-r,num))
    circle_list.append((x+r,-num))



heapq.heapify(circle_list)
parents = [[] for _ in range(N+1)]
stack = [0]

while circle_list:
    position, ind = heapq.heappop(circle_list)
    if ind < 0:
        stack.pop()
    else:
        parents[ind].append(stack[-1])
        stack.append(ind)

nodes = list(map(int,input().split()))
path_list = [[],[]]


for i in range(2):
    while nodes[i] != 0:
        path_list[i].append(nodes[i])
        nodes[i] = parents[nodes[i]][0]
    
    path_list[i].append(0)
mid_val = -1
answer = []
for ind,val in enumerate(path_list[0]):
    if val in path_list[1]:
        mid_val = val
        answer.append(val)
        break
    else:
        answer.append(val)
flag = False
for ind in range(len(path_list[1])-1,-1,-1):
    if flag:
        answer.append(path_list[1][ind])
    elif path_list[1][ind] == mid_val:
        flag = True


print(len(answer))
print(*answer)