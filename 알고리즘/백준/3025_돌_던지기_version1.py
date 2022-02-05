import sys
def input():
    return sys.stdin.readline().rstrip()
sys.setrecursionlimit(100000)
def move():
    return [[0,1],[2,1]]
def outOfBound(x,y):
    if 0<=x<R and 0<=y<C:
        return False
    return True


def throw(col):
    global start_col
    flag = False
    if len(last_idx[col]):
        while True:
            idx,col = last_idx[start_col].pop()
            if arr[idx][col] == '.':
                break
    else:
        idx = 0
    while idx <R-1:
        last_idx[start_col].append((idx,col))
        next_idx = idx + 1
        if arr[next_idx][col] == 'X':
            break
        if arr[next_idx][col] == 'O':
            flag =True
            for move_list in move():
                x,y = idx,col
                for d in move_list:
                    nx = x  + dx[d]
                    ny = y + dy[d]
                    if outOfBound(nx,ny) or arr[nx][ny] != '.':
                        break
                    x,y = nx,ny
                else:
                    col = y
                    idx = x
                    flag = False
                    break
        if flag:
            break
        idx = next_idx
    arr[idx][col] = 'O'



R,C = map(int,input().split())

dx = [0,1,0]
dy = [-1,0,1]
arr = [list(input()) for _ in range(R)]



N = int(input())
last_idx = [[] for _ in range(C)]
for f in range(N):
    start_col = int(input())-1
    throw(start_col)
for row in arr:
    sys.stdout.write(''.join(row)+'\n')