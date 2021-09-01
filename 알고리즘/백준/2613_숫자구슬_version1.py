import sys

def input():
    return sys.stdin.readline().rstrip()

def make_group(limit):
    temp = 0
    cnt = 0
    result = []
    group_cnt = K
    for ind in range(N):
        temp += arr[ind]
        if temp>limit:
            temp = arr[ind]
            result.append(cnt)
            group_cnt -= 1
            cnt = 0
        cnt += 1
        if group_cnt == (N-ind):
            result.append(cnt)
            group_cnt -= 1
            while group_cnt:
                result.append(1)
                group_cnt -= 1
            return result

def count_group(val):
    k = 0
    temp = 0
    for ind in range(N):
        temp += arr[ind]
        if temp>val:
            temp = arr[ind]
            k += 1
    if temp:
        k += 1
    return k


N,K = map(int,input().split())

arr = list(map(int,input().split())) 


left = max(arr)-1
right = sum(arr)
answer = right
while left+1<right:
    mid = (left+right)//2
    K_mid = count_group(mid)
    if K_mid > K:
        left = mid
    else:
        right = mid
print(right)
print(*make_group(right))