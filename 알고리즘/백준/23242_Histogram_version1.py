import sys
def input():
    return sys.stdin.readline().rstrip()
def variance_range(left,right):
    if nums_dict.get((left,right)):
        return nums_dict[(left,right)]
    square_average = (square_sum[right] - square_sum[left-1])/(right-left+1)
    averge_square = (prefix_sum[right] - prefix_sum[left-1])/(right-left+1)
    nums_dict[(left,right)] = (square_average - averge_square**2)*(right-left+1)
    return nums_dict[(left,right)]

def histogram(left_ind,remain_bucket):
    if dp[left_ind][remain_bucket] != -1:
        return dp[left_ind][remain_bucket]
    if remain_bucket == 1:
        dp[left_ind][remain_bucket] = variance_range(left_ind,N)
        return dp[left_ind][remain_bucket]
    min_val = float('inf')
    for right_ind in range(left_ind,N - remain_bucket+2):
        val = variance_range(left_ind,right_ind) + histogram(right_ind+1,remain_bucket-1)
        if val < min_val:
            min_val = val
    dp[left_ind][remain_bucket] = min_val
    return min_val
Bucket_Size = int(input())
N = int(input())

prefix_sum = [0 for _ in range(N+1)]
square_sum = [0 for _ in range(N+1)]
for ind in range(1,N+1):
    num = int(input())
    prefix_sum[ind] += prefix_sum[ind-1] + num
    square_sum[ind] += square_sum[ind-1] + (num**2)
cnt = 0
nums_dict = {}
dp = [[-1 for _ in range(Bucket_Size+1)] for _ in range(N+1)]
answer = float('inf')

print(f'{histogram(1,Bucket_Size):.6f}')