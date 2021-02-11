N,M = map(int,input().split())
arr = [[0]*(M+1)]
for _ in range(N):
    arr.append([0]+list(map(int,list(input()))))
result = 0
max_size = min(N,M)

for x in range(1,N+1):
    for y in range(1,M+1):
        if arr[x][y]:
            arr[x][y] = min(arr[x-1][y],arr[x][y-1],arr[x-1][y-1])+1
            result = max(arr[x][y],result)
        if result == max_size:
            break

print(result**2)
