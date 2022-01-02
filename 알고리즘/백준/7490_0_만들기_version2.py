import sys

def input():
    return sys.stdin.readline().rstrip()


def solve(total,now,idx,signal,string):
    if idx == N:
        total += now*signal
        if total == 0:
            print(string)
    else:
        solve(total,now*10+(idx+1),idx+1,signal,string + ' ' + str(idx+1))
        solve(total +(signal*now), idx+1, idx+1, 1, string + '+' + str(idx+1) )
        solve(total + (signal*now),idx+1, idx + 1,-1, string + '-' + str(idx+1) )



        

T = int(input())

for tc in range(T):
    N = int(input())

    result = []
    solve(0,1,1,1,'1')
    print()