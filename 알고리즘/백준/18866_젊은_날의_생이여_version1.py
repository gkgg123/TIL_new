import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

happy = []

piro = []


for i in range(N):
    x,y = map(int,input().split())
    happy.append(x)
    piro.append(y)
INF = float('inf')
# 최소 happy 최대 피로도
young_arr = [[INF,0] for _ in range(N+2)]

old_arr = [[0,INF] for _ in range(N+2)]

for i in range(1,N+1):
    young_arr[i][0] = young_arr[i-1][0]
    young_arr[i][1] = young_arr[i-1][1]
    if happy[i-1]:
        young_arr[i][0] = min(young_arr[i][0],happy[i-1])
    if piro[i-1]:
        young_arr[i][1] = max(young_arr[i][1],piro[i-1])

for i in range(N,-1,-1):
    old_arr[i][0] = old_arr[i+1][0]
    old_arr[i][1] = old_arr[i+1][1]
    if happy[i-1]:
        old_arr[i][0] = max(old_arr[i][0],happy[i-1])
    if piro[i-1]:
        old_arr[i][1] = min(old_arr[i][1],piro[i-1])



result = -1

for k in range(N-1,0,-1):
    if young_arr[k][0] > old_arr[k+1][0] and young_arr[k][1] < old_arr[k+1][1]:
        if result < k:
            result = k
            break
print(result)