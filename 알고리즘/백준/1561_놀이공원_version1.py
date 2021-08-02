import sys
import math
def input():
    return sys.stdin.readline().rstrip()
def check(mid):
    cnt = 0
    for time in arr:
        temp = math.ceil(mid/time)
        cnt += temp
    return cnt

N, M = map(int,input().split())

arr = list(map(int,input().split()))


left = 0
right = (N//M+1)*30+1

result = 0
while left+1<right:
    mid = (left+right)//2
    if check(mid)>=N:
        right = mid
    else:
        left = mid

result = 0
prev_person = check(right-1)
remain_cnt = N - prev_person
for i in range(M):
    temp = math.ceil(right/arr[i]) - math.ceil((right-1)/arr[i])
    if temp>0:
        remain_cnt -= temp
        if not remain_cnt:
            result = i
print(result+1)
