import sys
import math
def input():
    return sys.stdin.readline()


N,user_atk = map(int,input().split())


max_hp = 0
acc_hp = 0
# 데미지는 마이너스
# 힐은 플러스
damage_or_heal = 0


arr = [list(map(int,input().split())) for _ in range(N)]


for command,atk,hp in arr:
    if command == 1:
        atk_cnt = math.ceil(hp/user_atk)
        damage_or_heal = -(atk_cnt-1)*atk
    else:
        user_atk += atk
        damage_or_heal = hp
    
    acc_hp += damage_or_heal
    if acc_hp>0:
        acc_hp = 0
    max_hp = max(max_hp,abs(acc_hp))
print(max_hp+1)