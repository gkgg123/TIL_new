import sys

sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()
def dfs(idx,eat_list,eat,pay):
    global pay_min,result
    if pay >= pay_min:
        return
    for e_idx in range(4):
        if eat_list[e_idx] < eat_min[e_idx]:
            break
    else:
        if pay_min > pay:
            pay_min = pay
            result = eat
            return
    for e_idx in range(idx,N):
        new_eat_list = eat_list[:]
        for i in range(4):
            new_eat_list[i] += arr[e_idx][i]
        dfs(e_idx+1,new_eat_list,eat+' '+str(e_idx+1),pay+arr[e_idx][4])
    return
N = int(input())

eat_min = list(map(int,input().split())) 
arr = [list(map(int,input().split())) for _ in range(N)]



pay_min = float('inf')
result = -1
dfs(0,[0]*4,'',0)

if pay_min != float('inf'):
    print(pay_min)
    print(*result.split())
else:
    print(-1)