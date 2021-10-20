import sys
sys.setrecursionlimit(10000)
def input():
    return sys.stdin.readline().rstrip()
def checkodd(num):
    cnt = 0
    while num//10:
        cnt = cnt +  num%10%2
        num = num//10
    cnt += num%2
    return cnt

def solution(num):
    cur_odd = checkodd(int(num))
    if len(num) == 1:
        return [cur_odd, cur_odd]
    elif len(num) == 2:
        next_num = int(num[0]) + int(num[1])
        next_sol = solution(str(next_num))
        return [next_sol[0] + cur_odd, next_sol[1] + cur_odd]
        
    else:
        max_value = 0
        min_value = float('inf')
        for ind1 in range(1,len(num)-1):
            for ind2 in range(ind1+1,len(num)):
                next_num = int(num[:ind1]) + int(num[ind1:ind2]) + int(num[ind2:])
                next_sol = solution(str(next_num))
                max_value = max(max_value,next_sol[1])
                min_value = min(min_value,next_sol[0])
        return [min_value + cur_odd, max_value + cur_odd]

num = input()


print(*solution(num))