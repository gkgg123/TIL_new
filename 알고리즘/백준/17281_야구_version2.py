from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for _players in permutations(range(2,10)):
    _players = list(_players)
    players = _players[:3]+[1] + _players[3:]
    cu_player_ind = 0
    # 1루,2루,3루
    score = 0
    for innings in arr:
        out_count = 0
        base1,base2,base3 = 0,0,0
        while out_count<3:
            if innings[players[cu_player_ind]-1] == 0:
                out_count += 1
            elif innings[players[cu_player_ind]-1] == 1:
                
                score += base3
                base1,base2,base3 = 1,base1,base2
            elif innings[players[cu_player_ind]-1] == 2:
                score += (base2+base3)
                base1,base2,base3 = 0,1,base1
            elif innings[players[cu_player_ind]-1] == 3:
                score += (base1+base2+base3)
                base1,base2,base3 = 0,0,1
            else:
                score = score + base1+base2+base3 + 1
                base1,base2,base3 = 0,0,0
            cu_player_ind = (cu_player_ind+1)%9
    if score > result:
        result = score
print(result)