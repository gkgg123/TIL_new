import sys
sys.setrecursionlimit(20000)


def dfs(left_idx,right_idx,day):
    if left_idx > right_idx:
        return 0
    if dp[left_idx][right_idx] != -1:
        return dp[left_idx][right_idx]

    dp[left_idx][right_idx] = max(dp[left_idx][right_idx], dfs(left_idx+1,right_idx,day+1) + v[left_idx]*day , dfs(left_idx,right_idx-1,day+1) + v[right_idx]*day)
    return dp[left_idx][right_idx]
def input():
    return sys.stdin.readline().rstrip()

N = int(input())

v = [int(input()) for _ in range(N)]

dp = [[-1 for _ in range(N)] for _ in range(N)]


print(dfs(0,N-1,1))

