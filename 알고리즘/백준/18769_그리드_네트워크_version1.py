import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()
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

    if ranks[X]<ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X
    if ranks[X] == ranks[Y]:
        ranks[X] += 1
    return True

T = int(input())

answer = []
for _ in range(T):
    R,C = map(int,input().split())
    # R*C+C
    node_list = []
    for x in range(R):
        temp = list(map(int,input().split()))

        for y in range(C-1):
            _now = x*C+y
            _next = _now+1
            node_list.append((temp[y],_now,_next))


    for x in range(R-1):
        temp = list(map(int,input().split()))

        for y in range(C):
            _now = x*C+y
            _next = _now+C
            node_list.append((temp[y],_now,_next))

    make_set = [i for i in range(R*C)]
    ranks = [1 for _ in range(R*C)]
    result = 0
    cnt = 0
    node_list.sort(reverse=True)
    while node_list and cnt<R*C:
        dis,x,y = node_list.pop()

        if union(x,y):
            cnt += 1
            result += dis
    print(result)
