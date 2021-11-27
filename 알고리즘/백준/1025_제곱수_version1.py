import sys
def input():
    return sys.stdin.readline().rstrip()

def checksquare(num):
    s_num = int(num**0.5)
    if s_num*s_num == num:
        return True
    return False
def innerBound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
def solve(x,y,dx,dy):
    global result
    num = 0

    nx,ny = x,y
    while innerBound(nx,ny):
        num = num*10 + arr[nx][ny]
        nx += dx
        ny += dy
        if checksquare(num) and num>result:
            result = num
def Check(x,y):
    global result
    down_x = -x
    up_x = N-x
    left_y = -y
    right_y = M-y
    num = arr[x][y]
    if checksquare(num):
        result = max(result,num)
    for dx in range(down_x,up_x+1):
        for dy in range(left_y,right_y+1):
            if dx == 0 and dy == 0:
                continue
            solve(x,y,dx,dy)

    


N,M = map(int,input().split())
arr = [list(map(int,list(input()))) for _ in range(N)]
result = -1
for x in range(N):
    for y in range(M):
        Check(x,y)
print(result)