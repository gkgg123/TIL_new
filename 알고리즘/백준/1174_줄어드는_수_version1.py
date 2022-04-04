import sys

def input():
    return sys.stdin.readline().rstrip()

def dfs(digit,N):
    if digit == -1:
        return 0
    for idx in range(10):
        if N<= dp[digit][idx]:
            return idx*(10**digit)+ dfs(digit-1,N)
        N -= dp[digit][idx]
        

def solve(N):
    # 자리수
    digit = -1
    for i in range(10):
        # 0번째 자리수
        line_sum = sum(dp[i])
        if N<= line_sum:
            digit = i
            break
        else:
            N -= line_sum
    if digit == -1:
        return -1
    return dfs(digit,N)

N = int(input())


dp = [[1]*10 if i == 0 else [0]*10 for i in range(10)]


for i in range(1,10):
    for k in range(i,10):
        dp[i][k] = sum(dp[i-1][:k])


answer = solve(N)
print(answer)