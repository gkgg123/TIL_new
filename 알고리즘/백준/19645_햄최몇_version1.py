import sys


def input():
    return sys.stdin.readline().rstrip()


N = int(input())

arr = list(map(int,input().split()))

max_sum = sum(arr)
dp = [[False for _ in range(max_sum+2)] for _ in range(max_sum+2)]

dp[0][0] = True
for ham in arr:
    for first in range(max_sum,-1,-1):
        for second in range(max_sum,-1,-1):
            dp[first][second] |= (bool(dp[max(first-ham,-1)][second] or dp[first][max(second-ham,-1)]))



result = 0
for first in range(1,max_sum-1):
    for second in range(1,first+1):
        if dp[first][second] and second>=max_sum-first-second:
            result = max(result,max_sum-first-second)
print(result)