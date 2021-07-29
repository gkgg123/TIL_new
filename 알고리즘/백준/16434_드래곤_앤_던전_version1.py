import sys
import math
def input():
    return sys.stdin.readline().rstrip()

def check(max_hp):
    cu_atk = input_atk
    cu_hp = max_hp
    for command,atk,hp in arr:
        if command == 1:
            atk_cnt = math.ceil(hp/cu_atk)
            cu_hp -= (atk_cnt-1)*atk
            if cu_hp<=0:
                return False
        else:
            cu_atk += atk
            cu_hp += hp
            if cu_hp> max_hp:
                cu_hp = max_hp
    return True

N,input_atk = map(int,input().split())

arr = []


for _ in range(N):
    t,a,h = map(int,input().split())

    arr.append((t,a,h))

left = 0
right = 999999000001*123456


while left+1<right:
    mid = (left+right)//2
    if check(mid):
        right = mid
    else:
        left = mid
print(right)