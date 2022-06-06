import sys

def input():
    return sys.stdin.readline().rstrip()

def check(temp):
    cnt = len(temp)
    for x in range(cnt):
        val = 0
        for y in range(x,cnt):
            val += temp[y]
        if val > 10 or val<-10:
            return False
        if arr[x][cnt-1] == '+' and val<=0:
            return False
        if arr[x][cnt-1] == '0' and val != 0:
            return False
        if arr[x][cnt-1] == '-' and val>=0:
            return False
    return True


def dfs(queue):
    if len(queue) == N:
        print(*queue)
        exit()
        return
    next_idx = len(queue)
    if arr[next_idx][next_idx] == '0':
        temp = queue + [0]
        if check(temp):
            dfs(temp)
    elif arr[next_idx][next_idx] == '+':
        
        for num in range(1,11):
            temp = queue + [num]
            if check(temp):
                dfs(temp)
    else:
        for num in range(1,11):
            temp = queue + [-num]
            if check(temp):
                dfs(temp)
N = int(input())
st = input()
arr = [[-1 for _ in range(N)] for _ in range(N)]

answer = []
idx = 0
for i in range(N):
    for j in range(N):
        if j<i:
            continue
        arr[i][j] = st[idx]
        idx += 1

if arr[0][0] == '0':
    dfs([0])
elif arr[0][0] == '+':
    for num in range(1,11):
        dfs([num])
else:
    for num in range(1,11):
        dfs([-num])

