import sys

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
colors = [-1] + list(map(int,input().split()))


result = int(0 not in colors)


for _ in range(N-1):
    x,y = map(int,input().split())

    if colors[x] != colors[y]:
        result += 1

print(result)