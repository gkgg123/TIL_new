from collections import deque
import collections

start_point,end_point = map(int,input().split())



queue = deque()

queue.append(start_point)

dp = [-1 for _ in range(200001)]
dp[start_point] = 0
while queue:
    node = queue.popleft()

    if node == end_point:
        break
    
    for idx,val in enumerate([2*node,node-1,node+1]):
        if val<0 or val>50:continue
        if idx == 0:
            if dp[val] == -1 or dp[val] > dp[node]:
                dp[val] = dp[node]
                queue.appendleft(val)
        else:
            if dp[val] == -1 or dp[val] > dp[node] + 1:
                dp[val] = dp[node] + 1
                queue.append(val)
print(dp[end_point])