import sys

def input():
    return sys.stdin.readline().rstrip()

def check(gap,K,N):
    left = 0
    right = N-1
    cnt = 0
    while left <right:
        cur_val = arr[left] + arr[right]
        if abs(K - cur_val) <= gap:
            cnt += 1
        if cur_val > K:
            right -= 1
        else:
            left += 1
    return cnt


T = int(input())

for _ in range(T):
    N,K = map(int,input().split())

    left = -1
    right = 10**9
    arr = list(map(int,input().split()))
    arr.sort()
    result = float('inf')
    answer = 0
    while left + 1< right:
        mid = (left+right)//2

        cnt = check(mid,K,N)

        if cnt:
            right = mid
            if result > mid:
                result = mid
                answer = cnt
        else:
            left = mid
    print(answer)
