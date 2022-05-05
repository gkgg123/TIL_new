import sys
def input():
    return sys.stdin.readline().rstrip()

def find_parents(x):
    if x == make_set[x]:
        return x
    make_set[x] = find_parents(make_set[x])
    return make_set[x]


def union(x,y):
    X = find_parents(x)
    Y = find_parents(y)

    if X != Y:
        if ranks[X] < ranks[Y]:
            X,Y = Y,X
        make_set[Y] = find_parents(X)
        ranks[X] += ranks[Y]
        return True
    return False


N,M = map(int,input().split())
make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
result = 0
node_list = sorted([list(map(int, input().split())) for _ in range(M)], key=lambda x:x[2])
cnt = 0
for pay,x,y in node_list:

    if union(x,y):
        cnt += 1
        result += pay
    if cnt == N-2:
        break
print(result)