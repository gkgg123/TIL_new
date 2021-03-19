T = int(input())
dp = [[1]*10 if ind == 0 else [0]*10 for ind in range(64)]
result = [0]*64
result[0] = 10
for ind in range(1,64):
    for num in range(9,-1,-1):
        if num == 9:
            dp[ind][num] = result[ind-1]
        else:
            dp[ind][num] = dp[ind][num+1] - dp[ind-1][num+1]
    result[ind] = sum(dp[ind])

for _ in range(T):
    n = int(input())
    print(result[n-1])