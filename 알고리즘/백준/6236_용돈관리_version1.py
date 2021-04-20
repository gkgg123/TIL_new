N,M = map(int,input().split())
arr =  [ int(input()) for _ in range(N)]
left = max(arr)
right = 100000001
answer = float('inf')
while left<=right:
    mid = (left+right)//2
    temp = mid
    cnt = 1
    for num in arr:
        if temp >= num:
            temp -= num
        else:
            temp = mid - num
            cnt += 1
    
    if cnt >M:
        left = mid + 1
    else:
        right = mid - 1
        answer = min(answer,mid)

print(answer)


