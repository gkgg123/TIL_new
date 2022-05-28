import sys
def input():
    return sys.stdin.readline().rstrip()

def distance(x1,y1,x2,y2):
    return ((y1-y2)**2 + (x1-x2)**2)**0.5
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
    else:
        if ranks[X]<ranks[Y]:
            X,Y = Y,X
        make_set[Y] = X
        if ranks[X] == ranks[Y]:
            ranks[X] += 1
        return True
N = int(input())
stars = []

make_set = [i for i in range(N)]
ranks = [0 for _ in range(N)]
edge_list = []
for idx in range(N):
    x,y = map(float,input().split())
    for prev_star in range(idx):
        px,py = stars[prev_star]
        edge_list.append((distance(px,py,x,y),prev_star,idx)) 
    stars.append((x,y))
edge_list.sort(reverse=True)
cnt = 0
result = 0
while edge_list:
    if cnt == N-1:
        break
    cur_val,idx1,idx2 = edge_list.pop()

    if union(idx1,idx2):
        result += cur_val
        cnt += 1


print(f'{result:.2f}')