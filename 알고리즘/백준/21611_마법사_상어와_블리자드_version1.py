import sys
def input():
    return sys.stdin.readline().rstrip()
def init(x,y):
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
    cnt = 1
    dire = 0
    double_cnt = 0
    number_cnt = 1
    stack = []
    x = x + dx[dire]
    y = y + dy[dire]
    if arr[x][y]:
        stack.append(arr[x][y])
    while True:
        if cnt == number_cnt:
            cnt = 0
            double_cnt += 1
            dire = (dire+1)%4
            if double_cnt == 2:
                double_cnt = 0
                number_cnt += 1
        nx = x + dx[dire]
        ny = y + dy[dire]
        if 0>nx or nx>=N or 0>ny or ny>=N:break
        if arr[nx][ny]:
            stack.append(arr[nx][ny])
        x,y =nx,ny
        cnt += 1
    
    return stack


def blizzard(dire,s):
    global ball,center_x,center_y
    max_value = N**2
    dire -= 1
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    remove_list = []
    x = center_x + dx[dire]
    y = center_x + dy[dire]
    while s:
        p = min(x,y,N-x-1,N-y-1)
        if y>=x:
            q = x+y -2*p
        else:
            q = (N-1-2*p)*4-(x+y-2*p)
        q += 4*(p*N-(p*p))
        remove_idx = max_value - q-2
        if remove_idx >= len(ball):
            break
        remove_list.append(remove_idx)
        nx = x + dx[dire]
        ny = y + dy[dire]
        if 0>nx or nx>=N or 0>ny or ny>=N:break
        x = nx
        y = ny
        s -= 1
    for idx in reversed(remove_list):
        ball.pop(idx)

def bomb(ball):
    global result
    if not ball:
        return []
    while True:
        new_ball = []
        cnt = 0
        stack = []

        for num in ball:
            if stack:
                if stack[-1] != num:
                    if len(stack) >= 4:
                        result[stack[-1]] += len(stack)
                        cnt += 1
                        stack = [num]
                    else:
                        new_ball.extend(stack)
                        stack = [num]
                else:
                    stack.append(num)
            else:
                stack.append(num)
        if stack:
            if len(stack) >= 4:
                result[stack[-1]] += len(stack)
                cnt += 1
            else:
                new_ball.extend(stack)
        ball = new_ball[:]
        if not cnt:
            return ball

def reshape(ball):
    max_size = N*N-1
    new_ball = []
    stack = []
    for num in ball:
        if stack:
            if stack[-1] != num:
                new_ball.extend([len(stack),stack[-1]])
                stack = [num]
            else:
                stack.append(num)
        else:
            stack.append(num)
        if len(new_ball) >=max_size:
            return new_ball[:max_size]
    if stack:
        new_ball.extend([len(stack),stack[-1]])
    if len(new_ball) >=max_size:
            return new_ball[:max_size]
    return new_ball
        

    

N,M = map(int,input().split())

arr = [list(map(int,input().split())) for _ in range(N)]
center_x,center_y = N//2,N//2

ball = init(center_x,center_y)

result = [0]*4
for tc in range(M):
    dire,s = map(int,input().split())
    blizzard(dire,s)
    ball = bomb(ball)
    ball = reshape(ball)
    if max(ball)>=4:
        assert IndexError
        break
answer = 1*result[1] + 2*result[2] + 3*result[3]
print(answer)