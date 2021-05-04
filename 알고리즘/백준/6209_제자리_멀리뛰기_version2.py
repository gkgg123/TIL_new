import sys
input = sys.stdin.readline

D,N,M = map(int,input().split())


arr = [D] + [int(input()) for _ in range(N)]

arr.sort()
left = 0
right = D
ans = 0
while left<=right:
    mid = (left+right)//2
    past_island = 0
    cnt = 0
    for island in arr:
        if island - past_island >= mid:
            cnt += 1
            past_island = island
    
    if cnt >= N-M+1:
        ans = max(ans,mid)
        left = mid + 1
    else:
        right = mid -1

print(ans)