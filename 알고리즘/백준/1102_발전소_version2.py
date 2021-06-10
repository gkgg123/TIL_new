import sys

input = sys.stdin.readline

def dfs(state,order_cnt):
    if dp[state] != -1:
        return dp[state]
    if order_cnt >= P:
        dp[state] = 0
        return 0
    else:
        min_value = float('inf')
        for cu_node in range(N):
            if state & 1<<cu_node:
                for next_node in range(N):
                    if not state & 1<<next_node:
                        min_value = min(min_value,dfs(state|1<<next_node,order_cnt+1) + arr[cu_node][next_node])
        dp[state] = min_value
        return dp[state]

N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]


state_string = input()
state = 0
P = int(input())
order_cnt = 0
for i in range(N):
    if state_string[i] == 'Y':
        state += 1<<i
        order_cnt += 1
dp = [-1 for _ in range(2**N+1)]
if order_cnt >= P:
    print(0)
elif order_cnt == 0:
    if P:
        print(-1)
    else:
        print(0)
else:
    result = dfs(state,order_cnt)
    if result == float('inf'):
        print(-1)
    else:
        print(result)