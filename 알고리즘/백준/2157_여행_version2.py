import sys

def input():
    return sys.stdin.readline().rstrip()


N,M,K = map(int,input().split())

graph = [{} for  _ in range(N+1)]

for _ in range(K):
    x,y,pay = map(int,input().split())
    if x>y:
        continue
    graph[x][y] = max(graph[x].get(y,0),pay)


dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]

dp[1][1] = 0

for cur_node in range(1,N+1):
    for next_node in graph[cur_node]:
        for depth in range(1,M):
            if dp[cur_node][depth] < 0:
                continue
            dp[next_node][depth+1] = max(dp[next_node][depth+1],graph[cur_node][next_node] + dp[cur_node][depth])


print(max(dp[N]))