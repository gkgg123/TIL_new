import sys
def input():
    return sys.stdin.readline().rstrip()

N,B,C = map(int,input().split())
ramen = list(map(int,input().split()))
buy_C = [0 for _ in range(N)]
result = 0
if C<B:
    for idx in range(N):
        if idx > 0:
            buy_C[idx] = min(ramen[idx-1],ramen[idx])
            ramen[idx] -= buy_C[idx]
            result += C*buy_C[idx]
            
        if idx -1>0:
            min_val = min(buy_C[idx-1],ramen[idx])
            result += C*min_val
            ramen[idx] -= min_val
        
        result += ramen[idx]*B
else:
    result = sum(ramen)*B
print(result)

