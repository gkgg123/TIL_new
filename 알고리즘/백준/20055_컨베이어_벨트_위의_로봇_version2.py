
n, k = list(map(int,input().split()))
conveyer = list(map(int,input().split()))
robot = [0]*n
robot_cnt = 1
step = 0
while conveyer.count(0) < k:
    last_number = conveyer.pop()
    conveyer.insert(0,last_number)
    last_robot = robot.pop()
    robot.insert(0,0)
    robot[n-1] = 0
    que = []
    for i in range(n):
        if robot[i] > 0:
            que.append([robot[i],i])
    que.sort()
    while que:
        robot_ind, ind = que.pop(0)
        if ind + 1 == n-1:
            if conveyer[n-1] != 0:
                robot[ind+1] = 0
                robot[ind] = 0
                conveyer[n-1] -= 1
            else:
                robot[ind] = robot_ind 
        else:
            if conveyer[ind+1] != 0 and robot[ind+1]==0:
                robot[ind+1] = robot_ind
                robot[ind] = 0
                conveyer[ind+1] -= 1
            else:
                robot[ind] = robot_ind
    if robot[0] == 0 and conveyer[0]:
        robot[0] = robot_cnt
        robot_cnt += 1
        conveyer[0] -= 1
    step += 1
print(step)


