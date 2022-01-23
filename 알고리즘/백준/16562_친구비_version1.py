import sys
import heapq
def find_parents(x):
    if make_set[x] == x:
        return x
    make_set[x] = find_parents(make_set[x])
    return make_set[x]

def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X == Y:
        return False
    if ranks[X] < ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X

    if ranks[X] == ranks[Y]:
        ranks[X] += 1
    return True

def input():
    return sys.stdin.readline().rstrip()


N,M,K = map(int,input().split())

coins = [0]+list(map(int,input().split()))

make_set = [i for i in range(N+1)]

ranks = [1 for _ in range(N+1)]

cnt = 0
for _ in range(M):
    x,y = map(int,input().split())
    union(x,y)

node_list = []

for ind in range(1,N+1):
    node_list.append((coins[ind],ind))
heapq.heapify(node_list)

total = 0
while node_list:
    pay,x = heapq.heappop(node_list)
    if union(0,x):
        total += pay

if total>K:
    print("Oh no")
else:
    print(total)