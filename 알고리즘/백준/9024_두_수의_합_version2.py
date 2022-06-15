import sys

def input():
    return sys.stdin.readline().rstrip()


T = int(input())

result = []
for _ in range(T):
    N,K = map(int,input().split())
    arr = list(map(int,input().split()))
    arr.sort()
    min_val = float('inf')
    cnt = 0
    left = 0
    right = N-1
    while left<right:
        cur_val = arr[left] + arr[right]
        cur_gap = abs(K-cur_val)
        if cur_val >= K:
            right -= 1
        else:
            left += 1
        if cur_gap < min_val:
            min_val = cur_gap
            cnt = 1
        elif cur_gap == min_val:
            cnt += 1
    result.append(str(cnt))
sys.stdout.write('\n'.join(result))