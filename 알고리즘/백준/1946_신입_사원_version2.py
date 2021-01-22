import sys

T = int(input())

for tc in range(T):
    N = int(input())
    result = 1
    arr = [0]*(N+1)
    for _ in range(N):
        x,y = map(int,sys.stdin.readline().split())
        arr[x] = y
    min_value = arr[1]
    for ind in range(2,N+1):
        if min_value > arr[ind]:
            min_value = arr[ind]
            result += 1
    print(result)