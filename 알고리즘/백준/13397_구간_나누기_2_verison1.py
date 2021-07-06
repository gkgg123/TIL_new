import sys

def input():
    return sys.stdin.readline().rstrip()


def check(mid):
    idx = 0
    temp = []
    cnt = 0
    while idx<N:
        if cnt >M:
            return False
        if temp:
            min_value,max_value = min(temp),max(temp)
            if abs(arr[idx]-min_value)>mid or abs(arr[idx]-max_value)>mid:
                cnt += 1
                temp = [arr[idx]]
            else:
                temp.append(arr[idx])
        else:
            temp.append(arr[idx])
        idx += 1
    if temp:
        cnt += 1
    if cnt>M:
        return False
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

