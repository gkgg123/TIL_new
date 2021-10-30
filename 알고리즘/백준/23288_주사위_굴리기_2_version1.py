import sys
from collections import deque
def input():
    return sys.stdin.readline().rstrip()

def bfs(x,y,cnt):
    score = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    index_arr[x][y] = cnt
    visited[x][y] =True
    queue = deque()
    queue.append((x,y))
    stan = arr[x][y]
    while queue:
        x,y = queue.popleft()
        score += arr[x][y]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == stan and not visited[nx][ny]:
                    visited[nx][ny] = True
                    index_arr[nx][ny] = cnt
                    queue.append((nx,ny))
    return score


def roll(direction):
    global dice
    if direction == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif direction == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif direction == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    else:
        dice[0] , dice[1] , dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
def innerOfBound(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    return False
def move(dire):
    x,y = dice_position
    nx = x + dx[dire]
    ny = y + dy[dire]
    if innerOfBound(nx,ny):
        return [(nx,ny),dire]
    dire = (dire+2)%4
    nx = x + dx[dire]
    ny = y + dy[dire]
    return [(nx,ny),dire]

def get_score(position):
    x,y = position
    return sum_list[index_arr[x][y]]
def curve(dire,position):
    x,y = position
    if dice[-1] > arr[x][y]:
        return (dire+1)%4
    elif dice[-1] < arr[x][y]:
        return (dire-1)%4
    else:
        return dire
N,M,K = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
dx = [0,1,0,-1]
dy = [1,0,-1,0]
index_arr = [[-1 for _ in range(M)] for _ in range(N)]
sum_list = []
cnt = 0
for x in range(N):
    for y in range(M):
        if index_arr[x][y] == -1:
            sum_list.append(bfs(x,y,cnt))
            cnt += 1

dice = [1,2,3,4,5,6]
dire = 0
# 동,남,서,북
# [4,2,1,6,5,3]
# [2,6,3,4,1,5]
# [3,2,6,1,5,4]
# [5,1,3,4,6,2]
dice_position = [0,0]
result = 0
while K>0:

    dice_position,dire = move(dire)
    roll(dire)
    result += get_score(dice_position)
    dire = curve(dire,dice_position)
    K -= 1
print(result)