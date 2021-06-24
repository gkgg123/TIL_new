import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()



def find_parents(X):
    if X == make_set[X]:
        return X
    make_set[X] = find_parents(make_set[X])
    return make_set[X]


def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)

    if X !=Y:
        if ranks[X]< ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
    return False
N,M = map(int,input().split())

edge_list = deque()
result = [0 for _ in range(N)]
make_set = [i for i in range(N)]
ranks = [1 for _ in range(N)]

city_cnt = 0
for x in range(N):
    temp = list(input())
    for y in range(x+1,N):
        if temp[y] == 'Y':
            if union(x,y):
                city_cnt += 1
                result[x] += 1
                result[y] += 1
            else:
                edge_list.append((x,y))


if city_cnt<N-1 or city_cnt+len(edge_list)<M:
    print(-1)
else:
    remain_cnt = M - city_cnt

    while remain_cnt>0:
        x,y = edge_list.popleft()
        result[x] += 1
        result[y] += 1
        remain_cnt -= 1
    print(*result)