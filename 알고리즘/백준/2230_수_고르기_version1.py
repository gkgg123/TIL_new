import sys

def input():
    return sys.stdin.readline().rstrip()


def solve():
    arr = [int(input()) for _ in range(N)]
    arr.sort()
    left = 0
    right =1
    ans = float('inf')

    while left<N and right <N:
        if arr[right] - arr[left] >=M:
            ans = min(ans,arr[right] - arr[left])
            left += 1
            if ans == M:
                return ans
        else:
            right += 1
    return ans


N,M= map(int,input().split())


print(solve())