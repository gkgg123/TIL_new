from collections import deque

def roll(direction,red,blue):
    global arr,visited
    stack = deque()
    red = [*red,True]
    blue = [*blue,True]
    stack.append((red,blue))
    while stack:
        r,b = stack.popleft()

        r_x,r_y,r_state = r
        b_x,b_y,b_state = b
        visited[r_x][r_y] = False
        if r_state:
            nr_x = r_x + dx[direction]
            nr_y = r_y + dy[direction]
            if 0<=nr_x<N and 0<=nr_y<M:
                if nr_x == b_x and nr_y == b_y:
                    if not b_state:
                        r_state = False
                else:
                    if arr[nr_x][nr_y] == '#':
                        r_state = False
                    elif arr[nr_x][nr_y] == 'O':
                        r_state = False
                        r_x = -1
                        r_y = -1
                    else:
                        r_x = nr_x
                        r_y = nr_y
        if b_state:
            nb_x = b_x + dx[direction]
            nb_y = b_y + dy[direction]
            if 0<=nb_x<N and 0<=nb_y<M:
                if nb_x == r_x and nb_y == r_y:
                    if not r_state:
                        b_state = False
                else:
                    if arr[nb_x][nb_y] == '#':
                        b_state = False
                    elif arr[nb_x][nb_y] == 'O':
                        b_state = False
                        b_x = -1
                        b_y = -1
                    else:
                        b_x = nb_x
                        b_y = nb_y
        
        if not r_state and not b_state:
            if b_x == -1:
                return -1
            if r_x == -1:
                return 1
            return [r_x,r_y,b_x,b_y]
        
        stack.append(([r_x,r_y,r_state],[b_x,b_y,b_state]))


def bfs(r,b,g):
    global arr
    stack = deque()
    stack.append((r,b,0))
    visited[r[0]][r[1]] = False
    while stack:
        red,blue,cnt = stack.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nx = red[0] + dx[i]
            ny = red[1] + dy[i]
            if 0<=nx<N and 0<=ny<M:
                result = roll(i,red,blue)
                if type(result) == int:
                    if result == 1:
                        return cnt+1
                else:
                    nr = [result[0],result[1]]
                    nb = [result[2],result[3]]
                    stack.append((nr,nb,cnt+1))
    return -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]


N,M = map(int,input().split())

arr = []
red_ball = []
blue_ball = []
goal = []
visited = [[True]*M for _ in range(N)]
for x in range(N):
    temp = list(input())

    for y in range(M):
        if temp[y] == 'R':
            temp[y] = '.'
            red_ball = [x,y]
        elif temp[y] == 'B':
            temp[y] = '.'
            blue_ball = [x,y]
        elif temp[y] == 'O':
            goal = [x,y]
    arr.append(temp)
print(bfs(red_ball,blue_ball,goal))
