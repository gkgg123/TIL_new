import sys
from math import acos, atan2,cos,sin,pi
def input():
    return sys.stdin.readline().rstrip()


def distance(p1,p2):
    return ((p1[0] - p2[0])**2 + (p1[1]-p2[1])**2)**0.5
def angle_between(p1,p2):
    return atan2(p2[1]-p1[1],p2[0]-p1[0])

def calc(p1,p2):
    return (p1[0]*p2[0] +p1[1]+p2[1])/((p1[0]**2 + p1[1]**2)**0.5 * (p2[0]**2 + p2[1]**2)**0.5)
def check(mid):
    global r_x,r_y
    for x in range(N):
        inner_list = {}
        for y in range(N):
            if x == y:continue
            if distance_two_points[x][y] > 2*mid:
                continue
            inner_angle = acos(distance_two_points[x][y]/(2*mid))
            start_angle = angle_two_points[x][y] - inner_angle
            end_angle = angle_two_points[x][y] + inner_angle
            if start_angle<0:
                start_angle += 2*pi
                end_angle += 2*pi
    
            inner_list[start_angle] = inner_list.get(start_angle,0) + 1
            inner_list[end_angle]  = inner_list.get(end_angle,0) -1
        sum_points = 1
        for key in sorted(inner_list.keys()):
            sum_points += inner_list[key]
            if sum_points >= K:
                r_x = points[x][0] + cos(key)*mid
                r_y = points[x][1] + sin(key)*mid
                return True
    
    return False

left_radius = 0
right_radius = 20000

N, K = map(int,input().split())


points = []

for _ in range(N):
    x,y = map(int,input().split())
    points.append((x,y))


distance_two_points = [[0 for _ in range(N)] for _ in range(N)]

angle_two_points = [[0 for _ in range(N)] for _ in range(N)]
for x in range(N):
    for y in range(N):
        if x == y:continue
        distance_two_points[x][y] = distance(points[x],points[y])
        angle_two_points[x][y] = angle_between(points[x],points[y])

r_x = -1
r_y = -1
for _ in range(50):
    mid = (left_radius+right_radius)/2
    if check(mid):
        right_radius = mid
    else:
        left_radius = mid

print(f'{right_radius}')
print(r_x,r_y)