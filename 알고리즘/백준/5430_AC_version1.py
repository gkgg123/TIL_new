import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def pop(queue,flag):
    if flag:
        return queue.pop()
    else:
        return queue.popleft()
T = int(input())

for _ in range(T):
    commands = list(input())
    N = int(input())
    if N:
        arr = deque(input().replace('[','').replace(']','').split(','))
    else:
        input()
        arr = deque()
    # 0 정방향 1 역방향
    flow = 0
    flag = True
    for command in commands:
        if command == 'R':
            flow = (flow+1)%2
        else:
            if arr:
                pop(arr,flow)
            else:
                flag = False
                break
    if flag:
        if flow:
            arr.reverse()
        print(f'[{",".join(arr)}]')
    else:
        print('error')
