N,S = map(int,input().split())
arr = list(map(int,input().split()))
start,end = 0,0
temp = 0
result = float('inf')

while start <= end:
    if temp >= S:
        temp = temp - arr[start]
        result = min(result,end - start)
        start += 1
    elif end == N:
        start += 1
    else:
        temp = temp + arr[end]
        end += 1
if result == float('inf'):
    print(0)
else:
    print(result)