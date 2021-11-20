import sys
import math
def input():
    return sys.stdin.readline().rstrip()


def get_slope(p1,p2):
    if p1.x == p2.x:
        return float('inf')
    return (p1.y - p2.y)/(p1.x - p2.x)

def get_ccw(p1,p2,p3):
    return ((p2.x - p1.x)*(p3.y-p1.y) - (p2.y - p1.y)*(p3.x - p1.x))
def distance(p1,p2):
    return ((p2.x-p1.x)**2 + (p2.y - p1.y)**2)**0.5
class Point():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y



N,L = map(int,input().split())

points = []

for _ in range(N):
    x,y = map(int,input().split())
    points.append(Point(x,y))
points.sort(key = lambda p : (-p.x,-p.y))

hull = [points.pop()]
points.sort(key= lambda p : (get_slope(p,hull[0]), p.x,p.y))


for point in points:
    while len(hull)>1 and get_ccw(hull[len(hull)- 2] , hull[len(hull) - 1], point)<=0:
        hull.pop()
    hull.append(point)


answer = 0
H = len(hull)
for i in range(H):
    prev_point, now_point, next_point = hull[(i-1)%H] , hull[i] , hull[(i+1)%H]
    distance1 = distance(now_point,next_point)
    distance2 = distance(now_point,prev_point)
    answer += distance1
    u = Point(next_point.x - now_point.x , next_point.y - now_point.y)
    v = Point(prev_point.x - now_point.x , prev_point.y - now_point.y)
    inner_product = u.x*v.x + u.y*v.y 
    product_dictance = distance1*distance2
    inner_angle = math.acos(inner_product/product_dictance)
    answer += (L*(math.pi - inner_angle))

print(round(answer))