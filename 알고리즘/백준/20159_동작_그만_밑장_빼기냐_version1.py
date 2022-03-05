import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))



forward_sum = [0 for _ in range(N//2+2)]
back_sum = [0 for _ in range(N//2+2)]

for idx in range(N//2):
    back_idx = N-idx*2-1
    forward_sum[idx+1] = forward_sum[idx] + arr[2*idx]
    back_sum[idx+1] = back_sum[idx] + arr[back_idx]



result = 0

for i in range(N//2+1):
    result = max(result,forward_sum[i] + back_sum[-i-2])
    result = max(result,forward_sum[i] + back_sum[-i-1] - arr[-1])

print(result)