import sys


def input():
    return sys.stdin.readline().rstrip()

def solve(x,y):
    p = min(x,y,N-x-1,N-y-1)
    rx,ry = (N-p-1, N-p-1)
    lx,ly = (rx -(N-2*p-1) ,ry-(N-2*p-1))
    temp = 0
    base = 4*(p*N -(p*p))
    if x>=y:
        temp += rx - x + ry - y 
    else:
        temp += abs(x-lx) + abs(y-ly)
        temp += (rx-lx) + (rx-lx)
    return N*N - temp-base
N = 10001

r1,c1,r2,c2 = map(lambda x : x + 5000,map(int,input().split()))
max_value = 0
arr = []
for x in range(r1,r2+1):
    temp = []
    for y in range(c1,c2+1):
        temp.append(solve(x,y))

    arr.append(temp)
    max_value = max(max_value,max(temp))

max_len = len(str(max_value))
len_N = len(arr)
for idx,p in enumerate(arr):
    for num in p:
        print('%*d'%(max_len,num),end=' ')
    if len_N -1 != idx:
        print()
