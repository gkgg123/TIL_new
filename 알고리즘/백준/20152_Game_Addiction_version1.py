import sys
def input():
    return sys.stdin.readline().rstrip()

def solution(H,N):
    if H == N:
        return 1
    else:
        dp = [[0 if y != 0 else 1 for y in range(31)] for x in range(31)]
        K = abs(H-N)
        for y in range(1,K+1):
            for x in range(y,K+1):
                dp[x][y] = dp[x-1][y] + dp[x][y-1]
        return dp[K][K]

H,N = map(int,input().split())


print(solution(H,N))