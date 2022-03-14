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
    ranks[X] += ranks[Y]
    return False

N = int(input())

max_num = 10**6
make_set = [i for i in range(max_num+1)]
ranks = [1 for _ in range(max_num+1)]


for _ in range(N):
    command,*numbers = input().split()
    numbers = list(map(int,numbers))
    if command == 'I':
        union(numbers[0],numbers[1])
    else:
        print(ranks[find_parent(numbers[0])])