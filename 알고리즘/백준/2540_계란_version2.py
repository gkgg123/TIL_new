import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(copy_egg,D):
    global result,counts
    move = []
    remain_key = [0,1,2,3]
    remain_key.remove(D)
    while copy_egg.count(0) <3:
        A,B,C = sorted(remain_key,key= lambda x : copy_egg[x])
        if (sum(copy_egg) - copy_egg[D])%2:
            if not copy_egg[D]:
                return
            copy_egg[D] -= 1
            copy_egg[C] -= 1
            copy_egg[A] += 2
            move.append(copy_egg[:])
            continue

        if copy_egg[C] <= copy_egg[B] + copy_egg[A]:
            copy_egg[B] -= 1
            copy_egg[C] -= 1
            copy_egg[D] += 2 
        elif copy_egg[B]:
            copy_egg[C] -= 1
            copy_egg[B] -= 1
            copy_egg[A] += 2
        else:
            copy_egg[C] -= 1
            copy_egg[D] -= 1
            copy_egg[B] += 2
        move.append(copy_egg[:])
    if counts > len(move):
        result = [row[:] for row in move]
        counts = len(move)

K = int(input())
eggs = list(map(int,input().split()))
counts = float('inf')
result = []
for i in range(4):
    solve(eggs[:],i)


print(*eggs)
c = 0
for row in result:
    print(*row)
    c += 1
    if c == K:
        break