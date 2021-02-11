# 2493번 탑
from collections import deque
N = int(input())
arr =  list(map(int,input().split()))
result = [0]*N
stack = deque()
for ind in range(N):
    while stack and stack[len(stack)-1][1] < arr[ind]:
        stack.pop()
    if stack:
        result[ind] = stack[len(stack)-1][0]
    else:
        result[ind] = 0
    stack.append((ind+1,arr[ind])) 


    
print(*result)
