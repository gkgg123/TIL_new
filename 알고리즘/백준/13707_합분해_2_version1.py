import sys


def input():
    return sys.stdin.readline().rstrip()


N,K = map(int,input().split())

mod = 10**9
new_K = N+K-1
up_num = 1
down_num = 1

for i in range(N+1,new_K+1):
    up_num *= i
for i in range(1,new_K-N+1):
    up_num //=i
print(up_num%mod)   