import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
ramen_list = [[0 for _ in range(N)] for _ in range(3)]
ramen_list[0] = list(map(int,input().split()))
gap = 2
stan = 3
result = 0
for idx in range(N):
    result += (stan * ramen_list[0][idx])
    ramen_list[0][idx],ramen_list[1][idx] = 0,ramen_list[0][idx]

    if idx+1 <N:
        min_val = min(ramen_list[1][idx] , ramen_list[0][idx+1])
        result += (gap * min_val)
        ramen_list[1][idx] -= min_val
        ramen_list[0][idx+1] -= min_val
        ramen_list[2][idx] += min_val
    
    if idx - 1>=0 and idx+1<N:
        min_val = min(ramen_list[0][idx+1],ramen_list[2][idx-1])
        ramen_list[0][idx+1] -= min_val
        result += (gap*min_val)

print(result)