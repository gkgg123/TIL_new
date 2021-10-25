import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

def calc(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def find_parents(ind):
    if make_set[ind] == ind:
        return ind
    temp = find_parents(make_set[ind])
    make_set[ind] = temp
    return temp

def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)
    if X == Y:
        return True
    else:
        if ranks[X]<ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return False

N,M = map(int,input().split())

node_list = []
position = [[],]
for ind in range(1,N+1):
    x,y = map(int,input().split())
    for ind2 in range(1,len(position)):
        heapq.heappush(node_list,(calc(position[ind2],(x,y)),ind,ind2))
    position.append((x,y))


ranks = [1 for _ in range(N+1)]
make_set = [i for i in range(N+1)]
cnt = 0
for _ in range(M):
    x,y = map(int,input().split())
    if union(x,y):
        continue
    cnt += 1
result = 0
while node_list:
    pay,x,y = heapq.heappop(node_list)

    if union(x,y):
        continue
    result += pay
    cnt += 1

    if cnt == N-1:
        break

print(f'{result:.2f}')