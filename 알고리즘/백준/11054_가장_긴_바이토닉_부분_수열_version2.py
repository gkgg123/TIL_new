def find_lis(array):
    dp = [0]*len(array)

    for i in range(len(array)):
        dp[i] = 1
        for j in range(i+1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    return dp
def find_lds(array):
    dp = [0]*len(array)

    for i in range(len(array)-1,-1,-1):
        dp[i] = 1
        for j in range(i+1,len(array)):
            if array[i] > array[j]:
                dp[i] = max(dp[i],dp[j] + 1)
    return dp
        




N = int(input())

arr = list(map(int,input().split()))

lis_dp = find_lis(arr)
lds_dp = find_lds(arr)

result = 0
for ind in range(N):
    result = max(result,lis_dp[ind]+lds_dp[ind]-1)
print(result)