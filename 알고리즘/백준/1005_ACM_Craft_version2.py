import sys
def input():
    return sys.stdin.readline().rstrip()
def solve(node):
    if spend_time[node] < 0:
        spend_time[node] = 0
        for parent in reverse_graph[node]:
            spend_time[node] = max(spend_time[node],solve(parent))
        spend_time[node] += times[node]
    return spend_time[node]
T = int(input())

for _ in range(T):
    N,K = map(int,input().split())
    times = [0] + list(map(int,input().split()))
    spend_time = [-1 for _ in range(N+1)]
    reverse_graph = [[] for _ in range(N+1)]
    for _ in range(K):
        x,y = map(int,input().split())
        reverse_graph[y].append(x)

    W = int(input())

    print(solve(W))