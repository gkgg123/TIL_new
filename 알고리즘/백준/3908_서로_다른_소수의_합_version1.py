import sys

def input():
    return sys.stdin.readline().rstrip()

def prime_nums(n):
    primes = [True for _ in range(n+1)]
    
    for num in range(2,int(n**0.5)+1):
        if primes[num]:
            for new_num in range(num*2,n+1,num):
                primes[new_num] = False
    result = []
    for num in range(2,n+1):
        if primes[num]:
            result.append(num)
    return result
max_N = 1120
max_k = 14
prime = prime_nums(max_N)

dp = [[0 for _ in range(max_N+1)] for _ in range(max_k+1)]
dp[0][0] = 1

for pn in prime:

    for n in range(max_N-pn,-1,-1):
        for ck in range(max_k,0,-1):
            if dp[ck-1][n]:
                dp[ck][n+pn] += dp[ck-1][n]

T = int(input())

for _ in range(T):
    N,k = map(int,input().split())

    print(dp[k][N])            