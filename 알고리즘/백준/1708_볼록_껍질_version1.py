import sys

class Point():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
    def __str__(self) -> str:
        return f'{self.x} {self.y}'


def input():
    return sys.stdin.readline().rstrip()

def get_slope(p1,p2):
    if p1.x == p2.x:
        return float('inf')
    return (p1.y-p2.y)/(p1.x-p2.x)
def get_ccw(p1,p2,p3):
    return ((p2.x - p1.x) *(p3.y - p1.y) - (p2.y - p1.y)*(p3.x - p1.x))
N = int(input())

points = []
for _ in range(N):
    x,y = map(int,input().split())
    points.append(Point(x,y))


points.sort(key= lambda p : (-p.x,-p.y))
hull = [points.pop()]
points.sort(key = lambda p : (get_slope(p,hull[0]),p.x,p.y))


for point in points:
    while len(hull)>1 and get_ccw(hull[len(hull)-2] , hull[len(hull)-1],point)<=0:
        hull.pop()
    hull.append(point)
print(len(hull))
for point in hull:
    print(point)