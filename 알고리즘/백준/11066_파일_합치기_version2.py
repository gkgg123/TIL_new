# # Knuth's Optimization
# # https://wogud6792.tistory.com/20

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    books = list(map(int,input().split()))
    prefix_sum = [0]*(N+1)
    INF = float('inf')
    dp =[[INF] *N for _ in range(N)]
    min_k_store_array = [[0]*N for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0
        min_k_store_array[i][i] = i
        prefix_sum[i+1] = prefix_sum[i] + books[i]
    for term in range(1,N):
        for i in range(N-term):
            j = term+i
            for k in range(min_k_store_array[i][j-1],min_k_store_array[i+1][j]+1):
                if k<N-1 and dp[i][j] > dp[i][k]+dp[k+1][j]+ prefix_sum[j+1] - prefix_sum[i]:
                    dp[i][j] = dp[i][k]+dp[k+1][j] + prefix_sum[j+1] - prefix_sum[i]
                    min_k_store_array[i][j] = k
    print(dp[0][N-1])
