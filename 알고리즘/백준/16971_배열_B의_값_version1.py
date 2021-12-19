import sys
sys.stdin = open('16971.in','r')
def input():
    return sys.stdin.readline().rstrip()

def change(array,move,fix):
    return maxs - array[move]//2 + array[fix]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for _ in range(N)]
rows = [0 for _ in range(N)]
cols = [0 for _ in range(M)]
for x in range(N):
    for y in range(M):
        if x == 0 or x ==N-1 or y== 0 or y==M-1:
            if (x == 0 or x ==N-1) and (y == 0 or y == M-1):
                rows[x] += arr[x][y]
                cols[y] += arr[x][y]
            else:
                rows[x] += 2*arr[x][y]
                cols[y] += 2*arr[x][y]
        else:
            rows[x] += 4*arr[x][y]
            cols[y] += 4*arr[x][y]

maxs = sum(rows)
result = maxs
for i in range(1,N-1):
    result = max(result,change(rows,i,0))
    result = max(result,change(rows,i,N-1))
    if result == 40510:
        print(i)
for i in range(1,M-1):
    result = max(result,change(cols,i,0))
    result = max(result,change(cols,i,M-1))
    if result == 40510:
        print(i)
        print(change(cols,i,M-1))
        break
print(result)