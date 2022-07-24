import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

result = 0
MIN_VALUE = -1000000001
px,py = MIN_VALUE,MIN_VALUE
for _ in range(N):
    x,y = map(int,input().split())

    if x > py:
        result += py - px
        px,py = x,y
    elif y > py:
        py = y
print(result + py-px)