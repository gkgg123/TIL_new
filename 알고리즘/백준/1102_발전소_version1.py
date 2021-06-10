import sys

input = sys.stdin.readline

def dfs(state,order_cnt):
    global result
    if order_cnt >= P:
        result = min(result,dp[state])
        return
    else:
        if dp[state] > result:
            return

        else:
            for cu_node in range(N):
                if state & 1<<cu_node:
                    for next_node in range(N):
                        if not state & 1<<next_node and dp[state|1<<next_node] > dp[state] + arr[cu_node][next_node]:
                            dp[state|1<<next_node] = dp[state] + arr[cu_node][next_node]
                            dfs(state|1<<next_node,order_cnt+1)



N = int(input())


arr = [list(map(int,input().split())) for _ in range(N)]


state_string = input()
state = 0
P = int(input())
order_cnt = 0
stack = []
result = float('inf')
for i in range(N):
    if state_string[i] == 'Y':
        state += 1<<i
        order_cnt += 1
        stack.append(i)
dp = [float('inf') for _ in range(2**N+1)]
dp[state] = 0
if order_cnt == P:
    print(0)
else:
    dfs(state,order_cnt)
    if result == float('inf'):
        print(-1)
    else:
        print(result)