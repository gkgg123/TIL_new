import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
stack = [0]
cnt = 0
for _ in range(N):
    x,y = map(int,input().split())

    while stack and stack[-1]>y:
        stack.pop()
        cnt += 1
    if stack[-1] != y:
        stack.append(y)
cnt += len(stack)-1
print(cnt)