import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def solve(s,t : deque):
    while len(s) != len(t):
        if t[-1] == 'A':
            t.pop()
        else:
            t.pop()
            t.reverse()
    if s == ''.join(t):
        return 1

    return 0
S = input()
T = deque(input())

print(solve(S,T))