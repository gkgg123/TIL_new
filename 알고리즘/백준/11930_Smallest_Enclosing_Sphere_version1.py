import sys
class Point():
    def __init__(self,x=0,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
    def add(self,x,y,z):
        self.x += x
        self.y += y
        self.z += z
    def normal(self,N):
        self.x = self.x/N
        self.y = self.y/N
        self.z = self.z/N
class Circle(Point):
    def __init__(self, x=0, y=0, z=0,r=0):
        super().__init__(x=x, y=y, z=z)
        self.r = r
    def update(self,point,ratio):
        self.x += (point.x - self.x) * ratio
        self.y += (point.y - self.y) * ratio
        self.z += (point.z - self.z) * ratio
    def __str__(self) -> str:
        return f'{self.r:.2f}'
def distance(a,b):
    return ((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2)**0.5
def isInner(cir,point):
    if distance(cir,point) <= cir.r:
        return True
    return False
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

points = []
C = Circle()
for _ in range(N):
    x,y,z = map(int,input().split())
    points.append(Point(x,y,z))
    C.add(x,y,z)
C.normal(N)
cnt = 20000
ratio = 0.1
while cnt>=0:
    pick_idx = 0
    C.r = 0
    for idx in range(N):
        dist = distance(C,points[idx])
        if C.r < dist:
            pick_idx = idx
            C.r = dist
    
    C.update(points[pick_idx],ratio)
    ratio *= 0.999
    cnt -= 1


print(C)