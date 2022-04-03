import sys

def input():
    return sys.stdin.readline().rstrip()

print = sys.stdout.write
def solve(x1,y1,x2,y2):
    print(f'{J[x2][y2] - J[x1-1][y2] - J[x2][y1-1] + J[x1-1][y1-1]} {O[x2][y2] - O[x1-1][y2] - O[x2][y1-1] + O[x1-1][y1-1]} {I[x2][y2] - I[x1-1][y2] - I[x2][y1-1] + I[x1-1][y1-1]}\n')
    return 

N,M = map(int,input().split())

K = int(input())

arr = [list(input()) for _ in range(N)]

J,O,I = [[[0 for _ in range(M+1)] for _ in range(N+1)] for _ in range(3)]

for x in range(N):
    for y in range(M):
        nx,ny = x+1,y+1
        if arr[x][y] == 'J':
            J[nx][ny] = 1
        elif arr[x][y] == 'O':
            O[nx][ny] = 1
        else:
            I[nx][ny] = 1


for x in range(1,N+1):
    for y in range(1,M+1):
        J[x][y] = J[x][y] + J[x-1][y] + J[x][y-1] - J[x-1][y-1]
        O[x][y] = O[x][y] + O[x-1][y] + O[x][y-1] - O[x-1][y-1]
        I[x][y] = I[x][y] + I[x-1][y] + I[x][y-1] - I[x-1][y-1]

for _ in range(K):
    x1,y1,x2,y2 = map(int,input().split())

    solve(x1,y1,x2,y2)