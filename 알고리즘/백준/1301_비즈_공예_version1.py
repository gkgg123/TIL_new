import sys

def input():
    return sys.stdin.readline().rstrip()
def dfs(t_idx,b_idx):
    global arr
    if dp[arr[1]][arr[2]][arr[3]][arr[4]][arr[5]][t_idx][b_idx] != -1:
        return dp[arr[1]][arr[2]][arr[3]][arr[4]][arr[5]][t_idx][b_idx]
    if sum(arr) == 0:
        return 1
    temp = 0
    for i in range(1,N+1):
        if arr[i] == 0:
            continue
        if i == t_idx or b_idx == i:
            continue
        arr[i] -= 1
        temp += dfs(b_idx,i)
        arr[i] += 1
    dp[arr[1]][arr[2]][arr[3]][arr[4]][arr[5]][t_idx][b_idx] = temp
    return temp
N = int(input())
arr = [0 for _ in range(6)]
for i in range(1,N+1):
    arr[i] = int(input())
dp = [[[[[[[-1 for _ in range(6)] for _ in range(6)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)] for _ in range(11)]

result = 0

for i in range(1,N+1):
    for j in range(1,N+1):
        if i == j:
            continue
        if arr[i] > 0 and arr[j]>0:
            arr[i] -= 1
            arr[j] -= 1
            result += dfs(i,j)
            arr[i] += 1
            arr[j] += 1
print(result)