import sys

def input():
    return sys.stdin.readline().rstrip()

M,N,L = map(int,input().split())


sade = list(map(int,input().split()))

sade.sort()

result = 0


for _ in range(N):
    x,y = map(int,input().split())
    if y>L:
        continue
    lower = x-L+y
    upper = x+L-y

    left = -1
    right = M
    while left+1<right:
        mid = (left+right)//2

        if lower<=sade[mid]<=upper:
            result += 1
            break
        if sade[mid]<lower:
            left = mid
        elif sade[mid]>upper:
            right = mid

print(result)