from collections import deque

N,K = map(int,input().split())

stack = deque(range(1,N+1))
result = []
while stack:
    stack.rotate(-(K-1))
    result.append(str(stack.popleft()))
print(f'<{", ".join(result)}>')
    