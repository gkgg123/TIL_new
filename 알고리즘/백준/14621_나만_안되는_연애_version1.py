import sys


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
    if ranks[X] < ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X
    if ranks[X] == ranks[Y]:
        ranks[X] += 1


N,M = map(int,input().split())

arr = [0] + list(input().split())
weight_list = []
for _ in range(M):
    x,y,pay = map(int,input().split())
    if arr[x] != arr[y]:
        weight_list.append((pay,x,y))

weight_list.sort(reverse=True)
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]

cnt = 0
result = 0
while weight_list:
    pay,x,y = weight_list.pop()
    X,Y = find_parents(x), find_parents(y)

    if X != Y:
        union(X,Y)
        cnt += 1
        result += pay
    if cnt == N-1:
        break

if cnt != N-1:
    print(-1)
else:
    print(result)