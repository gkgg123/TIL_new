import sys
def input():
    return sys.stdin.readline().rstrip()


class Point():
    def __init__(self,x=None,y=None):
        self.x = x
        self.y = y

class Circle(Point):
    def __init__(self, x=None, y=None,r = None):
        super().__init__(x=x, y=y)
        self.r = r

def get_ccw(p1,p2,p3):
    return ((p2.x - p1.x) * (p3.y - p1.y)) - ((p2.y-p1.y) *(p3.x -p1.x))

def make_Circle(p1,p2,p3):
    A = p2.x - p1.x
    B = p2.y - p1.y
    C = p3.x - p1.x
    D = p3.y - p1.y
    E = A*(p1.x + p2.x) + B*(p1.y + p2.y)
    F = C*(p1.x + p3.x) + D*(p1.y + p3.y)
    G = 2*(A*(p3.y - p2.y) - B*(p3.x-p2.x))
    if G == 0:
        return Circle()
    Center_Point = Point((D*E-B*F)/G , (A*F-C*E)/G)
    return Circle(Center_Point.x, Center_Point.y,distance(Center_Point,p1))
def distance(p1,p2):
    return ((p1.x-p2.x)**2 + (p1.y-p2.y)**2)**0.5

def isInner(c,p):
    if distance(c,p) <=c.r:
        return True
    return False    
def solve():
    C = Circle()
    for p1 in range(N):
        if (C.r == None or not isInner(C,points[p1])):
            C = Circle(points[p1].x,points[p1].y,0)  
            for p2 in range(p1+1):
                if not isInner(C,points[p2]):
                    new_C = Circle((points[p1].x + points[p2].x)/2, (points[p1].y + points[p2].y)/2 , distance(points[p1],points[p2])/2)
                    if new_C.r == 0:
                        C = new_C
                        continue
                    left_Circle , right_Circle = Circle(),Circle()

                    for p3 in range(p2+1):
                        if isInner(new_C,points[p3]):
                            continue
                        ccw_value = get_ccw(points[p1] , points[p2], points[p3])
                        instance_C = make_Circle(points[p1], points[p2], points[p3])
                        if instance_C.r == None:
                            continue
                        if ccw_value > 0 and (left_Circle.r == None or (get_ccw(points[p1], points[p2], instance_C) > get_ccw(points[p1], points[p2] ,left_Circle))):
                            left_Circle = instance_C
                        elif ccw_value < 0 and (right_Circle.r == None or (get_ccw(points[p1], points[p2], instance_C) < get_ccw(points[p1], points[p2], right_Circle))):
                            right_Circle = instance_C

                    if left_Circle.r == right_Circle.r == None:
                        C = new_C
                    elif left_Circle.r == None:
                        C = right_Circle
                    elif right_Circle.r == None:
                        C = left_Circle
                    else:
                        C = left_Circle if left_Circle.r <= right_Circle.r else right_Circle
    return C      

N = int(input())
points = []
remove_duplicate = set()
for _ in range(N):
    x,y = map(float,input().split())
    if (x,y) not in remove_duplicate:
        points.append(Point(x,y))
        remove_duplicate.add((x,y))


result = solve()
answer = result.r*2
print(f'{answer:.2f}')