import sys
def input():
    return sys.stdin.readline().rstrip()


def isBlack(x,y,max_size):

    cur_size = max_size
    cx,cy = x,y

    while cur_size//N:
        s = (N-K)*cur_size//N/2
        e = s+K*cur_size//N
        if s<=cx<e and s<=cy<e:
            return True

        cur_size//=N
        cx = cx - (cx//cur_size)*cur_size
        cy = cy - (cy//cur_size)*cur_size
    return False
times,N,K,r1,r2,c1,c2 = map(int,input().split())

max_size = N**times


arr = [['0' for _ in range(c2+1-c1)] for _ in range(r2+1-r1)]


for x in range(r1,r2+1):
    for y in range(c1,c2+1):
        if isBlack(x,y,max_size):
            arr[x-r1][y-c1] = '1'


for row in arr:
    print(''.join(row))