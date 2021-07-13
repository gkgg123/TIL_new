import sys
from collections import deque
def input():
    return sys.stdin.readline()
N,M = map(int,input().split())

sams = list(map(int,input().split()))

visited_set = set(sams)

queue = deque()
for sam in sams:
    queue.append((sam,0))

cnt = 0
result = 0
while queue:
    cur_node,dis = queue.popleft()
    result += dis
    cnt += 1
    if cnt == N+M:
        break
    for next_node in [cur_node+1,cur_node-1]:
        if next_node not in visited_set:
            visited_set.add(next_node)
            queue.append((next_node,dis+1))
print(result)
