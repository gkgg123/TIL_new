import sys
import math
def input():
    return sys.stdin.readline().rstrip()


def sol(num,cnt):
    for k in range(10**cnt):
        new_num = num*(10**cnt) + k
        if not new_num%lc:
            return new_num

    return sol(num,cnt+1)


N = input()
lc = 1

for n in set(N):
    if n == '0':
        continue
    lc = math.lcm(lc,int(n))
print(sol(int(N),0))