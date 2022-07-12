import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())

dice = list(map(int,input().split()))

if N == 1:
    print(sum(dice)-max(dice))
else:
    paint3 = 4
    paint2 = 8*N-12
    paint1 = (N-2) + 4*(N-2)*(N-1)
    dice[0] = min(dice[0],dice[5])
    dice[1] = min(dice[1],dice[4])
    dice[2] = min(dice[2],dice[3])
    result = paint1*min(dice) + paint2 * (sum(dice[:3]) - max(dice[:3])) + paint3*sum(dice[:3])
    print(result)