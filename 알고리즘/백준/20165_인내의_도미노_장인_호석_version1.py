import sys
def input():
    return sys.stdin.readline().rstrip()
def attack(x,y,d):
    long = domino[x][y]
    cnt = 1
    for rm in range(1,long):
        nx = x + dx[d]*rm
        ny = y + dy[d]*rm
        if not (0<=nx<N and 0<=ny<M):
            break
        if state[nx][ny] == 'F':
            continue
        cnt += attack(nx,ny,d)
    state[x][y] = 'F'
    return cnt

N,M,R = map(int,input().split())

dire = {'E':0,'W':1,'S':2,'N':3}
dx = [0,0,1,-1]
dy = [1,-1,0,0]

domino = [list(map(int,input().split())) for _ in range(N)]

state = [['S' for _ in range(M)] for _ in range(N)]

val = 0
for ind in range(2*R):
    if ind%2:
        # 방어
        x,y = map(int,input().split())
        state[x-1][y-1] = 'S'
    else:
        x,y,d = input().split()
        x,y = int(x)-1,int(y)-1
        if state[x][y] == 'S':
            val += attack(x,y,dire[d])

print(val)

for row in state:
    print(*row)