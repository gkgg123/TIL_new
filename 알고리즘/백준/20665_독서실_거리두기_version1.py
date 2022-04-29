import sys

def input():
    return sys.stdin.readline().rstrip()
def convert(a):
    hh,mm = a[:2],a[2:]
    return int(hh)*60 + int(mm) - 9*60

def find(idx,st):
    min_distance = float('inf')
    min_idx = 0
    for i in range(N):
        if idx == i:
            continue
        elif seat[i][st]:
            if abs(i-idx) < min_distance:
                min_distance = abs(i-idx)
    return min_distance
def solve(idx):
    if idx == T:
        return
    else:
        st,ed,gap = times[idx]
        max_value = 0
        max_seat = 0
        for s in range(N):
            if seat[s][st]:
                continue
            else:
                find_distance = find(s,st)
                if find_distance > max_value:
                    max_value = find_distance
                    max_seat = s
        for t in range(st,ed):
            seat[max_seat][t] = 1
        solve(idx+1)

N,T,P = map(int,input().split())
times = []
P -= 1
for _ in range(T):
    x,y = input().split()
    st,ed = convert(x),convert(y)
    times.append((st,ed,ed-st))
times.sort(key= lambda x : (x[0],x[2]))
seat = [[0 for _ in range(721)] for _ in range(N)]


solve(0)

print(720-sum(seat[P]))