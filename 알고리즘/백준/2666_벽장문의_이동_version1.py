def checkminNumber(index,open1,open2):
    if index > M-1:
        return 0 
    result = dp[index][open1][open2]
    if result != float('inf'):
        return result
    next_open = output_list[index]
    dp[index][open1][open2] = min(abs(open1 - next_open) + checkminNumber(index+1,next_open,open2), abs(open2 - next_open) + checkminNumber(index+1,open1,next_open))
    return dp[index][open1][open2]



N = int(input())

open1,open2 = list(map(int,input().split()))

M = int(input())
dp = [[[float('inf')]*(N+1) for _ in range(N+1)] for _ in range(M)]
output_list = []

for _ in range(M):
    output_list.append(int(input()))
print(checkminNumber(0,open1,open2))
