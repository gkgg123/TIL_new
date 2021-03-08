import sys
input = sys.stdin.readline

T = int(input())

def divide_two(ind_X,ind_Y):
    if ind_X == ind_Y:
        return books[ind_X]
    cache_data = dp[ind_X][ind_Y]
    if cache_data != -1:
        return cache_data

    temp = float('inf')
    mid_sum = prefix_sum[ind_Y+1] - prefix_sum[ind_X]
    for k in range(ind_X,ind_Y):
        temp = min(temp,divide_two(ind_X,k)+divide_two(k+1,ind_Y)+mid_sum)
    dp[ind_X][ind_Y] = temp
    return temp

    

for _ in range(T):

    N = int(input())
    dp = [[-1]*N for _ in range(N)]
    books = list(map(int,input().split()))
    prefix_sum = [0]*(N+1)
    for i in range(1,N+1):
        prefix_sum[i] = prefix_sum[i-1] + books[i-1]
    result = float('inf')

    for i in range(N-1):
        result = min(result,divide_two(0,i)+divide_two(i+1,N-1))

    print(result)