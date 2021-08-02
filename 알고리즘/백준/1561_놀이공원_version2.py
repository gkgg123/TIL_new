import sys

def input():
    return sys.stdin.readline().rstrip()

def check(mid):
    if mid<0:return 0
    cnt = 0
    for t in range(1,31):
        cnt += (mid//t*time_list[t])
    return cnt + M
N,M = map(int,input().split())

time_list = [0 for _ in range(31)]
arr = list(map(int,input().split()))
for t in arr:
    time_list[t] += 1
left = -1
right = (N//M+1)*30+1

while left+1<right:
    mid = (left+right)//2

    if check(mid)>=N:
        right = mid
    else:
        left = mid


remain_cnt = N - check(right-1)
for i in range(M):
    if not right%arr[i]:
        remain_cnt -= 1
        if not remain_cnt:
            print(i+1)
            break