import sys
def input():
    return sys.stdin.readline().rstrip()


S = list(input())

stack = []
lens = 0
prev_bracket = 0
for n in S:
    if n.isdigit():
        lens += 1
        prev_bracket = int(n)
    elif n == '(':
        stack.append((prev_bracket,lens-1))
        lens = 0
    else:
        multi_N, prevLens = stack.pop()

        lens = (multi_N*lens) + prevLens


print(lens)