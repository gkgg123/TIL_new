import sys

def find_agent(agent,task):
    if agent == N:
        return 1
    
    if dp[task] != -1:
        return dp[task]

    for i in range(N):
        if not (task & 1<<i):
            dp[task] = max(dp[task],find_agent(agent+1,task|1<<i)*arr[agent][i])
    
    return dp[task]
input = sys.stdin.readline
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]


dp = [-1 for _ in range(2**N+1)]




find_agent(0,0)

print(dp[0]/(100**N)*100)