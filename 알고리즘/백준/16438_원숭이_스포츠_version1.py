import sys

def input():
    return sys.stdin.readline().rstrip()

def solve(left,right,day,team):
    global arr
    if day == 7:
        return
    mid = (left+right)//2
    for idx in range(left,right):
        if idx<mid:
            arr[day][idx] = team
        else:
            arr[day][idx] = (team+1)%2
    solve(left,mid,day+1,team)
    solve(mid,right,day+1,(team+1)%2)
N = int(input())

arr = [[-1 for _ in range(N)] for _ in range(7)]
solve(0,N,0,0)

for row in arr:
    for y in range(N):
        print('A' if row[y] == 0 else 'B',end='')
    print()