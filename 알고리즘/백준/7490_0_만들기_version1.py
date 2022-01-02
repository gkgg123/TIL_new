import sys

def input():
    return sys.stdin.readline().rstrip()

def calc(arr):
    global result
    re = eval(''.join(arr))
    if re == 0:
        for idx in range(len(arr)):
            if arr[idx] == '':
                arr[idx] = ' '
        result.append(''.join(arr))


def solve(idx,arr):
    if idx == N-1:
        calc(arr)
    else:
        solve(idx+1,arr+['+']+[str(idx+2)])
        solve(idx+1,arr+['-']+[str(idx+2)])
        solve(idx+1,arr+['']+[str(idx+2)])
        

T = int(input())

for tc in range(T):
    N = int(input())

    result = []
    solve(0,['1'])
    result.sort()
    for row in result:
        print(row)
    if tc != T-1:
        print()