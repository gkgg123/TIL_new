import sys
from collections import defaultdict
sys.setrecursionlimit(2000)
def input():
    return sys.stdin.readline().rstrip()

def factorial(k):
    if memo[k]:
        return memo[k]
    else:
        memo[k] = (k*factorial(k-1))
        return memo[k]
    



memo = defaultdict(int)
memo[0] = 1
memo[1] = 1
N = int(input())
mod = 1000000007
cnt = 0
if N >1:
    for i in range(N):
        k = (1*i + (N-1-i)*2+2)%3
        if k == 0:
            cnt = cnt + factorial(N-1)//(factorial(i)*factorial(N-1-i))%mod
            cnt %= mod

print(cnt)