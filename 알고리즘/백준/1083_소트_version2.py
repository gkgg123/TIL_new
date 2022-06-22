import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
arr = list(map(int,input().split()))
S = int(input())

for st in range(N):
    max_val = arr[st]
    max_idx = st
    for ed in range(st+1,st+S+1):
        if ed>=N:
            break
        if max_val < arr[ed]:
            max_val = arr[ed]
            max_idx = ed
    
    S -= max_idx - st
    while max_idx > st:
        arr[max_idx] = arr[max_idx-1]
        max_idx -= 1
    arr[st] = max_val
print(*arr)