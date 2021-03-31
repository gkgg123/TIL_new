N = int(input())

arr = list(map(int,input().split()))

arr.reverse()
result = [-1]
stack = [arr[0]]

idx = 1
while idx <N:
    while stack and stack[-1] <= arr[idx]:
        stack.pop()
    if stack:
        result.append(stack[-1])
    else:
        result.append(-1)
    stack.append(arr[idx])
    idx += 1
result.reverse()
print(*result)