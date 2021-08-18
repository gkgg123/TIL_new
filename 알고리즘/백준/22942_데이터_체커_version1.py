import sys
def input():
    return sys.stdin.readline().rstrip()
def data_input():
    data = set()
    for idx in range(N):
        x,r = map(int,input().split())
        if x-r in data or x+r in data:
            return False
        arr.append((x-r, idx, 1))
        arr.append((x+r, idx, 0))
    return True

def check():
    stack = []

    for _, idx, isfirst in arr:
        if isfirst:
            stack.append(idx)
        elif stack[-1] != idx:
            return 'NO'
        else:
            stack.pop()
    return 'YES'
N = int(input())
arr = []

if data_input():
    arr.sort()
    print(check())
else:
    print('NO')

