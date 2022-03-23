import sys

def input():
    return sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N,M,T = map(int,input().split())
    arr = list(map(int,input().split()))

    arr = arr[:] + arr[:]
    left = 0
    right = 0
    result = 0 
    cnt = 0
    if N == M:
        N = 1
    while left<N:
        cnt += arr[right]
        right += 1
        if right - left == M:
            if cnt <T:
                result += 1
            cnt -= arr[left]
            left += 1
    print(result)