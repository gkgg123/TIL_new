import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(s):
    if s == S:
        print(1)
        exit()
    if len(s)<=len(S):
        return 0
    if s[-1] == 'A':
        solve(s[:-1])
    if s[0] == 'B':
        solve(s[-1:0:-1])
S = input()
T = input()
solve(T)
print(0)
