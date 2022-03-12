import queue
import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()
def find_parent(x):
    if make_set[x] == x:
        return x
    make_set[x] = find_parent(make_set[x])
    return make_set[x]

def union(x,y):
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        return True
    if ranks[X] < ranks[Y]:
        X,Y = Y,X
    make_set[Y] = X
    if ranks[X] == ranks[Y]:
        ranks[X] += 1
    return False

N,M = map(int,input().split())


make_set = [i for i in range(N+1)]
ranks = [1 for _ in range(N+1)]
enemy = [0 for _ in range(N+1)]
flag = True
for i in range(M):
    x,y = map(int,input().split())
    X = find_parent(x)
    Y = find_parent(y)
    if X == Y:
        flag = False
        break
    X_enemy = enemy[X]
    Y_enemy = enemy[Y]
    if X_enemy:
        union(Y,X_enemy)
    else:
        enemy[X] = Y
    
    if Y_enemy:
        union(X,Y_enemy)
    else:
        enemy[Y] = X

print(int(flag))