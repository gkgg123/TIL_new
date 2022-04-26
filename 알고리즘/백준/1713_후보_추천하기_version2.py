import sys
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
M = int(input())
command = list(map(int,input().split()))

sajin = []
recommand = []

for co in command:
    if co in sajin:
        recommand[sajin.index(co)] += 1
    else:
        if len(recommand) >= N:
            remove = recommand.index(min(recommand))
            sajin.pop(remove)
            recommand.pop(remove)
        sajin.append(co)
        recommand.append(1)

sajin.sort()
print(*sajin)