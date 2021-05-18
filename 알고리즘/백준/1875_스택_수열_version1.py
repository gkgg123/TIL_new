

N = int(input())
arr = [int(input()) for _ in range(N)]
stack = []
result = []
idx = 0
for i in range(1,N+1):
    stack.append(i)
    result.append('+')
    while stack and stack[-1] == arr[idx]:
        stack.pop()
        result.append('-')
        idx += 1

if stack:
    print('NO')
else:
    for i in result:
        print(i)