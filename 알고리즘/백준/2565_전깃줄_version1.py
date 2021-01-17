# 2565 전깃줄

N = int(input())
dp = [0]*501
arr = []
for _ in range(N):
    n1,n2 = map(int,input().split())
    arr.append((n1,n2))
arr.sort()
result = []
result.append(arr[0][1])
temp = 0
for k1,k2 in arr[1:]:
    for ind,val in enumerate(result):
        if val > k2 and k2 not in result:
            result[ind] =k2
            temp = 0
        elif val < k2 and k2 not in result:
            temp = k2
    if temp:
        result.append(temp)
    temp = 0


print(N-len(result))