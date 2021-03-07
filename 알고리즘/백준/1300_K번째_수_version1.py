N = int(input())
K = int(input())
ST,EN = 1,K
while ST<=EN:
    mid = (ST+EN)//2
    cnt = 0
    for i in range(1,N+1):
        cnt += min(mid//i,N)

    if cnt < K:
        ST = mid + 1
    else:
        EN = mid -1

print(ST)