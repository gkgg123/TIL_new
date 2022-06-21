import sys
def input():
    return sys.stdin.readline().rstrip()

def sol(x,y,n):
    if n == 3:
        stars[x][y] = '*'
        stars[x+1][y-1],stars[x+1][y+1] = '*','*'
        for i in range(-2,3):
            stars[x+2][y+i] = '*'
    else:
        n = n//2
        sol(x,y,n)
        sol(x+n,y-n,n)
        sol(x+n,y+n,n)
N = int(input())
stars = [[' ' for _ in range(2*N)] for _ in range(N)]
sol(0,N-1,N)

for row in stars:
    sys.stdout.write(''.join(row)+'\n')