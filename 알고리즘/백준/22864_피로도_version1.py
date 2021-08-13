import sys
import math
def input():
    return sys.stdin.readline()


A,B,C,M = map(int,input().split())

if M<A:
    print(0)
else:
    cur_pirodo = 0
    time = 0
    result = 0
    while time<24:
        if cur_pirodo + A > M:
            cur_pirodo -= C
            cur_pirodo = max(cur_pirodo,0)
        else:
            cur_pirodo += A
            result += B
        time += 1
    print(result)