import sys
from collections import defaultdict,deque
def input():
    return sys.stdin.readline().rstrip()


N = int(input())

graph = defaultdict(list)
pet_list = [0 for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
for next_node in range(2,N+1):
    pet,*arg = input().split()
    pay,island = map(int,arg)
    if pet == 'S':
        pet_list[next_node] = pay
    else:
        pet_list[next_node] = -pay
    graph[island].append(next_node)
    parents[next_node] = island

que = deque()
que.append(1)
stack = []
while que:
    cur_node = que.popleft()
    stack.append(cur_node)
    for next_node in graph[cur_node]:
        que.append(next_node)

while stack:
    cur_node = stack.pop()
    pet_list[parents[cur_node]] += max(0,pet_list[cur_node])

print(pet_list[0])

