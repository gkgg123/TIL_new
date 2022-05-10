import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
count = [0 for _ in range(N+1)]

for _ in range(N-1):
    x,y = map(int,input().split())
    count[x] += 1
    count[y] += 1

M = int(input())


for _ in range(M):
    x,y = map(int,input().split())
    if x == 2:
        print('yes')
    elif count[y] == 1:
        print('no')
    else:
        print('yes')