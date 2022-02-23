import sys
def input():
    return sys.stdin.readline().rstrip()

M = int(input())

left = 0
right = 500000001

flag = False
while left+1<right:
    mid = (left+right)//2
    cnt = 0
    mod = 5
    while mod<=mid:
        cnt += mid//mod
        mod *=5

    if cnt < M:
        left = mid
    else:
        if cnt == M:
            flag = True
        right = mid
if flag:
    print(right)
else:
    print(-1)