from datetime import datetime
from collections import defaultdict
import sys
input = sys.stdin.readline

def convert_L(L):
    day,arg = L.split('/')
    day = int(day)
    hour,min = map(int,arg.split(':'))
    total_min = min + hour*60 + day*24*60
    return total_min

N,L,F = list(input().split())
N = int(N)
F = int(F)
L = convert_L(L)
part_manager_dict = defaultdict(dict)

tardy_dict = defaultdict(int)
for _ in range(N):
    total_string = input()
    time_string = total_string[:16]
    time_S = datetime.strptime(time_string,'%Y-%m-%d %H:%M')
    part_name,person = total_string[16:].split()
    if part_manager_dict[person].get(part_name):
        borrowed_time = time_S - part_manager_dict[person][part_name]
        day = borrowed_time.days
        min = borrowed_time.seconds//60
        to_time = day*60*24 + min
        if to_time > L:
            tardy_dict[person] += (to_time-L)*F
        del part_manager_dict[person][part_name]
    else:
        part_manager_dict[person][part_name] = time_S


if len(tardy_dict.keys()):
    key_list = sorted(tardy_dict.keys())

    for key in key_list:
        print(key,int(tardy_dict[key]))

else:
    print(-1)