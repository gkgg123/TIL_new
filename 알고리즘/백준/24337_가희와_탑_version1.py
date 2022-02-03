import sys
def input():
    return sys.stdin.readline().rstrip()
def solve2():
    for idx in range(1,B+1):
        result[-idx] = idx
def solve1():
    for idx in range(base,A+base):
        result[idx] = idx-base+1
N,A,B = map(int,input().split())
base = N+2-(A+B)
result = [1 for _ in range(N+1)]
if A+B>N+1:
    print(-1)
else:
    if A<B:
        solve1()
        solve2()
    else:
        solve2()
        solve1()

    if A == 1:
        result[-B] = 1
        result[1] = B
    print(*result[1:])