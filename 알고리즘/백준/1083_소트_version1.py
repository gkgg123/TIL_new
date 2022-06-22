import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))


S = int(input())


for st in range(N-1):
    if not S:
        break
    max_val = arr[st]
    max_gap = 0
    for ed in range(st+1,N):
        gap = ed-st
        if gap >S:
            break
        if arr[ed] > max_val:
            max_val = arr[ed]
            max_gap = gap
    if max_gap:
        S -= max_gap
        arr.remove(max_val)
        arr.insert(st,max_val)

print(*arr)
