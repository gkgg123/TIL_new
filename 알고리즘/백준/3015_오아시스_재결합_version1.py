import sys
input = sys.stdin.readline

N = int(input())
result = [-1]*N
idx = 1
arr = [int(input()) for _ in range(N)]
result = 0
stack = [(arr[0],1)]
while stack and idx<N:
    acc = 1
    while stack and stack[-1][0]<=arr[idx]:
        if stack[-1][0] == arr[idx]:
            result += stack[-1][1]
            acc = stack[-1][1]+1
        else:
            result += stack[-1][1]
            acc = 1
        stack.pop()
    if stack:
        result += 1
    stack.append((arr[idx],acc))
    idx += 1


print(result)