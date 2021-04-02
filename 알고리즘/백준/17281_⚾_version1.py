from itertools import permutations
import sys
input = sys.stdin.readline
def play(entry):
    out_count = 0
    innings = 0
    cu_player_ind = 0
    # 1루,2루,3루
    score = 0
    base1,base2,base3 = 0,0,0
    while innings < N:
        while out_count<3:
            if arr[innings][entry[cu_player_ind]-1] == 0:
                out_count += 1
            elif arr[innings][entry[cu_player_ind]-1] == 1:
                
                score += base3
                base1,base2,base3 = 1,base1,base2
            elif arr[innings][entry[cu_player_ind]-1] == 2:
                score += (base2+base3)
                base1,base2,base3 = 0,1,base1
            elif arr[innings][entry[cu_player_ind]-1] == 3:
                score += (base1+base2+base3)
                base1,base2,base3 = 0,0,1
            else:
                score = score + base1+base2+base3 + 1
                base1,base2,base3 = 0,0,0
            cu_player_ind = (cu_player_ind+1)%9
        out_count = 0
        base1,base2,base3 = 0,0,0
        innings += 1
    return score





N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
result = 0
for _players in permutations(range(2,10)):
    _players = list(_players)
    players = _players[:3]+[1] + _players[3:]
    temp = play(players)
    if result <temp:
        result = temp
print(result)