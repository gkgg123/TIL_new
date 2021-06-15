import sys

input = sys.stdin.readline

N,M = map(int,input().split())

arr = list(map(int,input().split()))
cnt = [0]*(N+1)
for _ in range(M):
    command,x,y = map(int,input().split())
    x -= 1
    if command == 1:
        arr[x] = y
    elif command == 2:
        y -= 1
        for ind in range(x,y+1):
            arr[ind] = (arr[ind]+1)%2
    elif command == 3:
        y-=1
        for ind in range(x,y+1):
            arr[ind] = 0
    else:
        y -= 1
        for ind in range(x,y+1):
            arr[ind] = 1
print(*arr)
