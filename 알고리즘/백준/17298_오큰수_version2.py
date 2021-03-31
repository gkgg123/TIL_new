import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))
result = [-1]*N
stack = [0]
idx = 1
while stack and idx<N:
    while stack and arr[stack[-1]] < arr[idx]:
        result[stack.pop()] = arr[idx]
    stack.append(idx)
    idx += 1

print(*result)