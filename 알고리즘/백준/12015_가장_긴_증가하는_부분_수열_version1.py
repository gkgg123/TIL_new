N = int(input())
arr = list(map(int,input().split()))

LIS = [arr[0]]
for i in range(1,len(arr)):
    if arr[i] > LIS[-1]:
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

LIS_CNT = len(LIS)
print(LIS_CNT)