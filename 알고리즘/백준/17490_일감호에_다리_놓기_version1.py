import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def find_parents(ind):
    if make_set[ind] == ind:
        return ind
    make_set[ind] = find_parents(make_set[ind])
    return make_set[ind]
def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X == Y:
        return False
    if ranks[X] > ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X
    return True
    
N,M,K = map(int,input().split())

stons = list(map(int,input().split()))

stops = set()

for _ in range(M):
    x,y = map(int,input().split())
    stops.add((x-1,y-1))

node_list = []

for idx in range(N):
    x = idx
    y = (idx+1)%N
    if (x,y) in stops or (y,x) in stops:
        continue
    node_list.append((0,x,y))

heapq.heapify(node_list)
cnt = 0
make_set = [i for i in range(N)]
ranks = stons[:]
result = 0
while node_list:
    dis,x,y = heapq.heappop(node_list)
    if union(x,y):
        cnt += 1


parent_cnt = 0
for idx in range(N):
    if find_parents(idx) == idx:
        parent_cnt += 1
        result += ranks[idx]
if result<=K or parent_cnt<=1:
    print('YES')
else:
    print('NO')