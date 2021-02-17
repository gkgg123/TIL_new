# 6593 상범 빌딩
from collections import deque


def printresult(flag,sec):
    if flag:
        return f'Escaped in {sec} minute(s).'
    else:
        return 'Trapped!'


while True:
    L,R,C = map(int,input().split())
    if L+R+C == 0:
        break
    building = []
    dx = [-1,1,0,0,0,0]
    dy = [0,0,-1,1,0,0]
    dz  = [0,0,0,0,-1,1]
    startpoint = []
    endpoint = []
    for ind in range(L):
        temp = []
        for x in range(R):
            input_list = list(input())
            for y,val in enumerate(input_list):
                if val == 'S':
                    startpoint = [x,y,ind]
                elif val == 'E':
                    endpoint = (x,y,ind)
            temp.append(input_list)
        building.append(temp)
        input()
    # 층,행,열
    stack = deque()
    stack.append(startpoint)
    building[startpoint[2]][startpoint[0]][startpoint[1]] = '#'
    minutes = 0
    flag = False
    while stack:
        new_stack = []
        minutes += 1
        for x,y,z in stack:
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]
                if 0<=nx<R and 0<=ny<C and 0<=nz<L:
                    if building[nz][nx][ny] != '#':
                        if (nx,ny,nz) == endpoint:
                            flag = True
                            break
                        else:
                            building[nz][nx][ny] = '#'
                            new_stack.append((nx,ny,nz))
        if flag:
            print(printresult(flag,minutes))
            break

        stack = new_stack[:]
    if not flag:
        print(printresult(flag,minutes))

