import sys
input = sys.stdin.readline

T = int(input())

INF = 10**9
for _ in range(T):
    N = int(input())
    books = list(map(int,input().split()))
    prefix_sum = [0]*(N+1)
    dp =[[10**9] *N for _ in range(N)]
    min_k_store_array = list(range(N))
    for i in range(N):
        dp[i][i] = 0
        prefix_sum[i+1] = prefix_sum[i] + books[i]
    for term in range(1,N):
        new_arr = [None]*N
        for i in range(N-term):
            j = term+i
            for k in range(min_k_store_array[i],min(min_k_store_array[i+1]+1,j)):
                if dp[i][j] > dp[i][k]+dp[k+1][j]:
                    dp[i][j] = dp[i][k]+dp[k+1][j]
                    new_arr[i] = k

            dp[i][j] += prefix_sum[j+1] - prefix_sum[i]
        min_k_store_array = new_arr
    print(dp[0][N-1])
