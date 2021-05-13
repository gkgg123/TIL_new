# N: 방 크기
# M : 공팡이 개수
# K : 검사하는 개수
# t : 남은 일수
import sys

def input():
    return sys.stdin.readline().rstrip()
N,M,K,T = map(int,input().split())

mold = set()
visited = [[False]*N for _ in range(N)]
for _ in range(M):
    input_list = list(input().split())
    temp = []
    for check in input_list:
        if check.isdigit():
            temp.append(int(check))
    if len(temp)==2:
        mold.add((temp[0]-1,temp[1]-1))
        visited[temp[0]-1][temp[1]-1] = True
cleaning_place = []
for _ in range(K):
    input_list = list(input().split())
    temp = []
    for check in input_list:
        if check.isdigit():
            temp.append(int(check))
    if len(temp) == 2:
        cleaning_place.append((temp[0]-1,temp[1]-1))


dx = [-2,-1,1,2,2,1,-1,-2]
dy = [-1,-2,-2,-1,1,2,2,1]
time = 0
result = 'NO'
flag = False
while time <T:
    new_mold = set()
    for x,y, in mold:
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<N:
                visited[nx][ny] = True
                new_mold.add((nx,ny))
    time += 1
    cnt = 0
    for x,y in cleaning_place:
        if (x,y) in new_mold and (T-time)%2 == 0:
            result = 'YES'
            flag= True
            break
        elif (x,y) not in new_mold and visited[x][y]:
            cnt += 1
    else:
        if cnt == len(cleaning_place):
            flag = True
    if len(new_mold) == 0:
        flag = True
    mold = set(list(new_mold))
    if flag:
        break

print(result)

