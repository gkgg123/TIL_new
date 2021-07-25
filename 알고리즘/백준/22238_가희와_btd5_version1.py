import sys
from collections import defaultdict
def input():
    return sys.stdin.readline().rstrip()

def find_shoot_damage(x,y,damage):
    if arr[(x,y)]:
        left = -1
        right = len(arr[(x,y)])
        offset_damge = damage_list[(x,y)]
        find_hp = offset_damge + damage
        prev_cnt = kill_list[(x,y)]
        while left+1<right:
            mid = (left+right)//2

            if arr[(x,y)][mid]<=find_hp:
                left = mid
            else:
                right = mid
        damage_list[(x,y)] + damage
        if left == -1:
            return 0
        else:
            cur_cnt = left+1 - prev_cnt
            kill_list[(x,y)] += cur_cnt
            return cur_cnt
            
    return 0


def gcd(A,B):
    if not A%B:
        return B
    return gcd(B,A%B)
N,M = map(int,input().split())

arr = defaultdict(list)
for _ in range(N):
    x,y,hp = map(int,input().split())
    if x == 0 or y == 0:
        if x == 0:
            y = 1 if y>0 else -1
        else:
            x = 1 if x>0 else -1
    else:
       mod = gcd(abs(x),abs(y))
       x = x/mod
       y = y/mod
    
    arr[(x,y)].append(hp)

for key in arr:
    arr[key].sort()
damage_list = defaultdict(int)
kill_list = defaultdict(int)
for _ in range(M):
    x,y,damage = map(int,input().split())
    if N>0:
        if x == 0 or y == 0:
            if x == 0:
                y = 1 if y>0 else -1
            else:
                x = 1 if x>0 else -1
        else:
            mod = gcd(abs(x),abs(y))
            x = x/mod
            y = y/mod
        N -= find_shoot_damage(x,y,damage)
        print(N)
    else:
        print