import sys

def input():
    return sys.stdin.readline().rstrip()


def check(mid):
    min_value = arr[0]
    max_value = arr[0]
    idx = 1
    cnt = 1
    while idx<N:
        if cnt>M:
            return False
        if min_value>arr[idx]:
            min_value = arr[idx]
        if max_value < arr[idx]:
            max_value = arr[idx]
        
        if max_value-min_value>mid:
            min_value = arr[idx]
            max_value = arr[idx]
            cnt += 1
        idx += 1
    if cnt>M:
        return False
    else:
        return True
        

N,M = map(int,input().split())

arr = list(map(int,input().split()))


left = -1
right = 10001
while left+1<right:
    mid = (left+right)//2

    if check(mid):
        right = mid
    else:
        left = mid

print(right)

