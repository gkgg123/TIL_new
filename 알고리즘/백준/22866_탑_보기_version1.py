import sys

def input():
    return sys.stdin.readline()


N = int(input())

arr = list(map(int,input().split()))

tower_see =[0 for _ in range(N)]
tower_idx = [[float('inf'),-1] for _ in range(N)]
stack = [0]

idx = 1
while stack and idx <N:
    while stack and arr[stack[-1]] <= arr[idx]:
        stack.pop()
    tower_see[idx] += len(stack)
    if stack:
        if tower_idx[idx][0] > abs(idx - stack[-1]):
            tower_idx[idx][0] = abs(idx - stack[-1])
            tower_idx[idx][1] = stack[-1]
    stack.append(idx)
    idx += 1


stack = [N-1]
idx = N-2

while stack and idx >=0:
    while stack and arr[stack[-1]] <= arr[idx]:
        stack.pop()
    tower_see[idx] += len(stack)
    if stack:
        if tower_idx[idx][0] > abs(idx - stack[-1]):
            tower_idx[idx][0] = abs(idx - stack[-1])
            tower_idx[idx][1] = stack[-1]
    stack.append(idx)
    idx -= 1



for idx in range(N):
    if tower_see[idx]:
        print(tower_see[idx],tower_idx[idx][1]+1)
    else:
        print(0)