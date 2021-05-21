import sys

input = sys.stdin.readline

N = int(input())
edge = []
cost = []
def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    make_set[ind] = find_parent(make_set[ind])
    return make_set[ind]


def union(A,B):
    X = find_parent(A)
    Y = find_parent(B)

    if X != Y:
        if rank[X] < rank[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if rank[X] == rank[Y]:
            rank[X] += 1

for i in range(N):
    pay = int(input())
    edge.append((pay,0,i+1))
    cost.append(pay)

arr = [list(map(int,input().split())) for _ in range(N)]
for i in range(N):
    for j in range(i):
        edge.append((arr[i][j],i+1,j+1))



make_set = [i for i in range(N+1)]
rank = [0 for _ in range(N+1)]
edge.sort()
cnt = 0
result = 0
for pay,a,b in edge:
    if find_parent(a) != find_parent(b):
        cnt += 1
        result += pay
        union(a,b)
    if cnt == N:
        break
print(result)