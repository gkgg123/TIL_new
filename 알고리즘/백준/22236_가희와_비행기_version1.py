import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()


d,m = map(int,input().split())



prev_dp = {0:1}
next_dp = defaultdict(int)


for dis in range(1,d+1):
    if dis == d:
        for node in prev_dp:
            for next_node in [node-1,node+1]:
                next_dp[next_node]= (next_dp[next_node] + prev_dp[node])%m
    else:
        for node in prev_dp:
            for next_node in [node-1,node+1]:
                if next_node > 0:
                    next_dp[next_node]= (next_dp[next_node] + prev_dp[node])%m
        prev_dp = {}
        for key,val in next_dp.items():
            prev_dp[key] = val
        next_dp = defaultdict(int)


print(next_dp[0])