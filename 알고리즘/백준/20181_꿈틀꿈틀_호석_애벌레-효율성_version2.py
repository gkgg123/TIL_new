import sys

sys.setrecursionlimit(100001)
def find_min_right_over_k(left):
    global K
    low = left -1
    high = N
    while low + 1 < high:
        mid = (low+high)//2
        if prefix_sum[mid] - prefix_sum[left-1] >=K:
            high = mid
        else:
            low = mid
    return high




def solution(left):
    if left > N:
        return 0
    if dp[left] != -1:
        return dp[left]
    pass_hear_value = solution(left+1)
    right = find_min_right_over_k(left)
    eat_left_right = prefix_sum[right]-prefix_sum[left-1]-K+solution(right+1)
    max_value = max(pass_hear_value,eat_left_right)
    dp[left] = max_value
    return dp[left]

N,K = map(int,input().split())

arr = list(map(int,input().split()))

dp = [-1]*(N+1)

prefix_sum = [0]+arr[:]
for k in range(1,N+1):
    prefix_sum[k] += prefix_sum[k-1]


print(solution(1))
