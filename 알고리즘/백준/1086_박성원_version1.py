import sys

from math import factorial,gcd
def input():
    return sys.stdin.readline().rstrip()

def dfs(state,mod):
    if state == 2**N-1:
        if mod == 0:
            return 1
        return 0
    if dp[state][mod] != -1:
        return dp[state][mod]
    temp = 0

    for i in range(N):
        if state & (1<<i):continue
        temp += dfs(state|1<<i, (mod*tens_number[ size_ind[i]]+numbers[i] )%K)
    dp[state][mod] = temp
    return dp[state][mod]
N = int(input())
size_ind = [0 for _ in range(N)]
numbers = []
for ind in range(N):
    number = input()
    size_ind[ind] = len(number)
    numbers.append(int(number))

K = int(input())
tens_number = [1]
for i in range(50):
    tens_number.append(tens_number[-1]*10%K)

dp = [[-1 for _ in range(K+1)] for _ in range(2**(N+1))]
total_cnt = factorial(N)
result = dfs(0,0)

if result == 0:
    print('0/1')
elif result == total_cnt:
    print('1/1')
else:
    _gcd = gcd(total_cnt,result)
    total_cnt//=_gcd
    result//=_gcd
    print(f'{result}/{total_cnt}')