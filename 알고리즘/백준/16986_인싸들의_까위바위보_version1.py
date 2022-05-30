import sys
from itertools import permutations
def input():
    return sys.stdin.readline().rstrip()

def solve():
    p1,p2,p3 = 0,1,2
    wins = [0,0,0]
    turns = [0,0,0]
    while True:
        if p1>p2:
            p1,p2 = p2,p1
        if not p1 and turns[p1] >=N:
            break
        if turns[p1] >= 20 or turns[p2]>=20:
            break
        k1 = pattern[p1][turns[p1]]
        k2 = pattern[p2][turns[p2]]
        turns[p1] += 1
        turns[p2] += 1

        if arr[k1][k2] == 2:
            wins[p1] += 1
            p2,p3 = p3,p2
            if wins[p1] == K:
                break
        else:
            wins[p2] += 1
            p1,p3 = p3,p1
            if wins[p2] == K:
                break

    return wins[0]>=K


N,K = map(int,input().split())


arr =[list(map(int,input().split())) for _ in range(N)]

pattern = [[]]

for _ in range(2):
    temp = list(map(lambda x: x-1,map(int,input().split())))
    pattern.append(temp)

answer = 0
for pat in permutations(range(N)):
    pattern[0] = pat[:]

    if solve():
        answer = 1
        break

print(answer)

