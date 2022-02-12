import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

result = 0

stack = []
idx = 0
while idx<N:
    while stack and stack[-1] <= arr[idx]:
        stack.pop()
    result = result + len(stack)
    stack.append(arr[idx])
    idx += 1

print(result)


