N = int(input())
arr = list(map(int,input().split()))

result = [0]*N
stack = []

for ind in range(N-1,-1,-1):
    while stack and arr[stack[-1]] < arr[ind]:
        result[stack.pop()] = ind + 1
    stack.append(ind)

print(*result)