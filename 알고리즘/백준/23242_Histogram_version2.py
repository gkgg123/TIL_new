import sys
from functools import lru_cache
def input():
    return sys.stdin.readline().rstrip()

def variance_range(left,right):
    if number_dict.get((left,right)):
        return number_dict[(left,right)]
    averge_square = (prefix_sum[right] - prefix_sum[left-1])/(right-left+1)
    result = averge_square*averge_square * (right-left+1) + (square_sum[right] - square_sum[left-1]) - 2 * averge_square*(prefix_sum[right] - prefix_sum[left-1])
    number_dict[(left,right)] = result
    return result


Bucket_Size = int(input())
N = int(input())
prefix_sum = [0 for _ in range(N+1)]
square_sum = [0 for _ in range(N+1)]
dp = [[float('inf') for _ in range(Bucket_Size+1)] for _ in range(N+1)]
dp[0][0] = 0
for ind in range(1,N+1):
    num = int(input())
    prefix_sum[ind] += prefix_sum[ind-1] + num
    square_sum[ind] += square_sum[ind-1] + (num**2)

number_dict = {}
for right_idx in range(1,N+1):
    for left_idx in range(1,right_idx+1):
        temp = variance_range(left_idx,right_idx)

        for bucket in range(1,Bucket_Size+1):
            if dp[right_idx][bucket] > dp[left_idx-1][bucket-1] + temp:
                dp[right_idx][bucket] = dp[left_idx-1][bucket-1] + temp

print(f'{dp[N][Bucket_Size]:.6f}')