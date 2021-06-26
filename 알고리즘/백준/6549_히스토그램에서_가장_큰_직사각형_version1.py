import sys

input = sys.stdin.readline


while True:
    N,*arr = list(map(int,input().split()))

    if N == 0:
        break

    stack = [0]
    arr = [0] + arr[:] +[0]
    result = 0
    for ind in range(1,len(arr)):
        while stack and arr[ind] < arr[stack[-1]]:
            height = arr[stack[-1]]
            stack.pop()
            width = ind - stack[-1]-1
            result = max(result,height*width)
        stack.append(ind)

    print(result)