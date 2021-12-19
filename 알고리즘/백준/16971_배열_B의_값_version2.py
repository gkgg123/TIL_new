import sys
def input():
    return sys.stdin.readline().rstrip()

def change(array,max_length):
    if array[0] > array[max_length-1]:
        min_val = array[0]
        min_idx = 0
    else:
        min_val = array[max_length-1]
        min_idx = max_length-1
    for i in range(1,max_length-1):
        if array[i]//2 < min_val:
            min_val = array[i]//2
            min_idx = i
    if min_idx == 0 or min_idx == max_length-1:
        return maxs
    else:
        return max(maxs - min_val + array[0],maxs-min_val + array[max_length-1])

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
result = max(result,change(rows,N))
result = max(result,change(cols,M))
print(result)