import sys
def input():
    return sys.stdin.readline().rstrip()



N = int(input())
arr = list(map(int,input().split()))

cnt = 0
right = 0
visited = set()
for left in range(N):
    while right<N:
        if arr[right] in visited:
            break
        visited.add(arr[right])
        right += 1
    cnt = cnt + (right-left)
    visited.remove(arr[left])

print(cnt)