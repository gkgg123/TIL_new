N = int(input())
arr = list(map(int,input().split()))
LIS = [arr[0]]
parents = [-1]*N
parents[0] = 0
temp = 0
for i in range(1,len(arr)):
    if arr[i] > LIS[-1]:
        parents[i] = len(LIS)
        LIS.append(arr[i])
    else:
        start = 0
        end = len(LIS)
        idx = len(LIS)-1
        while start < end:
            mid = (start+end)//2
            if LIS[mid] >= arr[i]:
                idx = min(idx,mid)
                end = mid
            else:
                start = mid + 1
        LIS[idx] = arr[i]
        parents[i] = idx

LIS_CNT = len(LIS)
result = [-1]*LIS_CNT

for i in range(N-1,-1,-1):
    if parents[i] == LIS_CNT-1:
        result[LIS_CNT-1] = arr[i]
        LIS_CNT -= 1
print(len(result))
print(*result)
    
# https://jins-dev.tistory.com/entry/%EC%B5%9C%EC%A0%81%ED%99%94%EB%90%9C-LISLongest-Increasing-Subsequence-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98%EA%B3%BC-%ED%95%B4-%EC%B0%BE%EA%B8%B0