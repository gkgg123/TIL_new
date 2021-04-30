import sys
input = sys.stdin.readline

while True:
    N,M = map(int,input().split())

    arr = [[0] + list(map(int,input().split())) + [0] for i in range(N)]
    if N+M == 0:
        break
    for i in range(1,N):
        for j in range(1,M+1):
            if arr[i][j]:
                arr[i][j] = arr[i-1][j] + 1
    result = 0
    for i in range(N):
        stack = [0]
        for j in range(1,M+2):
            while stack and  arr[i][j] < arr[i][stack[-1]]:
                height = arr[i][stack[-1]]
                stack.pop()
                width = j-stack[-1] - 1
                result = max(result,height*width)
            stack.append(j)
    print(result)