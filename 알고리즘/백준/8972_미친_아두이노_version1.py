from collections import Counter

def move_robot(mad_ro,ro):
    new_robot = []

    for mad_x,mad_y in mad_ro:
        ro_distance = float('inf')
        ro_direction = -1
        for i in range(9):
            mad_nx = mad_x + dx[i]
            mad_ny = mad_y + dy[i]
            if 0<= mad_nx < R and 0<= mad_ny <C:
                distance = abs(mad_nx - ro[0]) + abs(mad_ny-ro[1])
                if ro_distance > distance:
                    ro_distance = distance
                    ro_direction = i

        new_x = mad_x + dx[ro_direction]
        new_y = mad_y + dy[ro_direction]
        new_robot.append((new_x,new_y))

    return new_robot
    
def bomb_robot(mad_ro):
    count_mad_ro = Counter(mad_ro)
    new_mad_ro = set()
    for key,value in count_mad_ro.items():
        if value == 1:
            new_mad_ro.add(key)
    return new_mad_ro




R,C = map(int,input().split())

arr = [list(input()) for _ in range(R)]

mad_robots = set()
robot = (0,0)
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'R':
            mad_robots.add((i,j))
            arr[i][j] = '.'
        elif arr[i][j] == 'I':
            robot = (i,j)
            arr[i][j] = '.'

command = list(map(lambda x : x-1, map(int,list(input()))))
dx = [1,1,1,0,0,0,-1,-1,-1]
dy = [-1,0,1,-1,0,1,-1,0,1]
flag = False
answer = 0
for time in range(len(command)):
    x,y = robot
    nx = x + dx[command[time]]
    ny = y + dy[command[time]]
    if (nx,ny) in mad_robots:
        flag =  True
        answer = time + 1
        break
    robot = (nx,ny)
    mad_robots = move_robot(mad_robots,robot)

    if robot in mad_robots:
        flag = True
        answer = time + 1
        break
    mad_robots = bomb_robot(mad_robots)


if flag:
    print(f'kraj {answer}')
else:
    arr[robot[0]][robot[1]] = 'I'
    for mad in mad_robots:
        arr[mad[0]][mad[1]] = 'R'

    for row in arr:
        print(''.join(row))