dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]


n,m,k = map(int,input().split())

fireball = {}

for _ in range(m):
    temp = list(map(int,input().split()))
    fireball[(temp[0]-1,temp[1]-1)] = []
    # 질량, 속도, 방향
    fireball[(temp[0]-1,temp[1]-1)].append([temp[2],temp[3],temp[4]])


for _ in range(k):
    new_fireball = {}
    for ind,vals in fireball.items():
        for val in vals:
            new_x = (ind[0] + val[1]*dx[val[2]])%n
            new_y = (ind[1] + val[1]*dy[val[2]])%n

            if new_fireball.get((new_x,new_y)):
                new_fireball[(new_x,new_y)].append([val[0],val[1],val[2]])
            else:
                new_fireball[(new_x,new_y)] = [[val[0],val[1],val[2]]]
    fireball ={}
    for ind,vals in new_fireball.items():
        if len(vals) > 1:
            total_weight = 0
            total_speed = 0
            total_direction = []
            for val in vals:
                total_weight += val[0]
                total_speed += val[1]
                total_direction.append(val[2])
            next_weight = total_weight//5
            next_speed = total_speed//len(vals)
            if next_weight:
                total_direction = list(map(lambda x: x%2 ,total_direction))
                if sum(total_direction) == 0 or sum(total_direction) == len(vals):
                    next_direction = [0,2,4,6]
                else:
                    next_direction = [1,3,5,7]
                fireball[ind] = []
                for i in range(4):
                    fireball[ind].append([next_weight,next_speed,next_direction[i]])

        else:
            fireball[ind] = vals

result = 0
for ind,vals in fireball.items():
    for val in vals:
        result += val[0]
print(result)