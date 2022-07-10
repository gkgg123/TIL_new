import sys

def input():
    return sys.stdin.readline().rstrip()


T = int(input())

for _ in range(T):
    x,y = map(int,input().split())
    distance = y-x
    n= 0
    while distance>(n+1)*n:
        n += 1

    if distance<=n**2:
        print(n*2-1)
    else:
        print(n*2)