import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ramen = list(map(int,input().split()))
buy_2 = [0 for _ in range(N)]
result = 0
for idx in range(N):
    if idx > 0:
        buy_2[idx] = min(ramen[idx-1],ramen[idx])
        ramen[idx] -= buy_2[idx]
        result += 2*buy_2[idx]
        
    if idx -1>0:
        min_val = min(buy_2[idx-1],ramen[idx])
        result += 2*min_val
        ramen[idx] -= min_val
    
    result += ramen[idx]*3
print(result)

