

N = int(input())

arr = list(map(int,input().split()))
dp = [*arr]
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]< arr[j]:
            dp[j] = max(dp[j],dp[i] + arr[j])

print(max(dp))