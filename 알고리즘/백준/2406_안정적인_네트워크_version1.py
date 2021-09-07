import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()
def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    make_set[ind] = find_parent(make_set[ind])
    return make_set[ind]

def union(x,y):
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        return False
    else:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True

N,M = map(int,input().split())

make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
connect_cnt = 0
for _ in range(M):
    x,y = map(int,input().split())
    if union(x,y):
        connect_cnt += 1

node_list = []

for x in range(N):
    temp = list(map(int,input().split()))

    for y in range(N):
        if x == 0 or y ==0 or x==y or x>y:
            continue
        else:
            node_list.append((temp[y],x+1,y+1))

if connect_cnt == N-2:
    print(0,0)
else:
    heapq.heapify(node_list)
    result = 0
    answer = []
    while node_list:
        pay,x,y = heapq.heappop(node_list)

        if union(x,y):
            result += pay
            connect_cnt += 1
            answer.append((x,y))
        if connect_cnt == N-2:
            break
    print(result,len(answer))
    for row in answer:
        print(*row)
