import sys
import bisect
def time_str_num(times):
    return times[:4]+times[5:7]+times[8:10]+times[11:13]+times[14:16]+times[17:19]

input = sys.stdin.readline

N,Q = map(int,input().split())

lev_list = [[] for _ in range(7)]
for _ in range(N):
    times,lev = input().split('#')
    times = time_str_num(times)
    lev_list[int(lev)].append(times)

result = []

for _ in range(Q):
    s_time,e_time,lev = input().split('#')

    s_time = time_str_num(s_time)
    e_time = time_str_num(e_time)
    lev = int(lev)
    cnt = 0
    for cu_lev in range(lev,7):
        s_ind = bisect.bisect_left(lev_list[cu_lev],s_time)
        e_ind = bisect.bisect_right(lev_list[cu_lev],e_time)
        cnt += (e_ind-s_ind)

    result.append(cnt)


for i in range(Q):
    sys.stdout.write(str(result[i])+'\n')