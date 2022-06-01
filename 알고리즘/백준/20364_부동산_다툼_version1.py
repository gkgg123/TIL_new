import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

occured = [False for _ in range(N+1)]

result = []
for _ in range(M):
    node = int(input())
    origin = node
    visit = 0
    while node != 1:
        if occured[node]:
            visit = node
        node = node//2
    if visit:
        result.append(str(visit))
    else:
        occured[origin] = True
        result.append("0")

sys.stdout.write('\n'.join(result))
