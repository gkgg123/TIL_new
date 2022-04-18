import sys

def input():
    return sys.stdin.readline().rstrip()
def range_check(x,y,k):
    if x+k<N and x-k>=0 and y+k<M and y-k >= 0:
        return True
    return False

def is_sharp(x,y,k):
    if arr[x-k][y] == arr[x+k][y] == arr[x][y-k] == arr[x][y+k] == '#':
        return True
    return False

def other():
    max_k = 0
    for x in range(N):
        for y in range(M):
            if arr[x][y] == '.':
                continue
            two_k = 0
            while range_check(x,y,two_k) and is_sharp(x,y,two_k):
                two_k += 1
            max_k = max(two_k-1,max_k)

    return max_k*4+1
N,M = map(int,input().split())

arr = [list(input()) for _ in range(N)]

result = 0
for x in range(N):
    for y in range(M):
        if arr[x][y] == '.':
            continue
        one_k = 0
        while range_check(x,y,one_k) and is_sharp(x,y,one_k):
            arr[x-one_k][y] = arr[x+one_k][y] = arr[x][y+one_k] = arr[x][y-one_k] = '.'

            area1 = 1 + one_k*4
            area2 = other()
            result = max(result,area1*area2)
            one_k += 1

        for k in range(one_k):
            arr[x-k][y] = arr[x+k][y] = arr[x][y+k] = arr[x][y-k] = '#'

print(result)