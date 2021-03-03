import sys

input = sys.stdin.readline
def union(A,B):
    x = find_parent(A)
    y = find_parent(B)
    if x > y:
        x,y = y,x
    make_set[y] = x

def find_parent(ind):
    if make_set[ind] == ind:
        return ind
    make_set[ind] = find_parent(make_set[ind])
    return make_set[ind]




V,E = map(int,input().split())

grpah = sorted([list(map(int,input().split())) for _ in range(E)],key=lambda x : x[2],reverse=True)

make_set = [i for i in range(V+1)]

cnt = 1 
result = 0

while cnt <V:
    p1,p2,weight = grpah.pop()
    if find_parent(p1) != find_parent(p2):
        union(p1,p2)
        result += weight
        cnt += 1

print(result)