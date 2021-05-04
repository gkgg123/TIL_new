import sys

input = sys.stdin.readline

D,N,M = map(int,input().split())

arr = [0]+[int(input()) for _ in range(N)]

arr.sort()
arr.append(D)
left = 0
right = D
ans = float('inf')
while left<=right:
    mid = (left+right)//2
    cnt = 0
    post_ind = 0
    for ind in range(1,N+2):
        if arr[ind] - arr[post_ind] <= mid:
            cnt += 1
        else:
            post_ind = ind
    
    if cnt > M:
        right = mid -1
    else:
        left = mid + 1

print(left)