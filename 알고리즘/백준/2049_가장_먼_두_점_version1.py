import sys
def input():
    return sys.stdin.readline().rstrip()
def get_slope(p1,p2):
    if p1[0] == p2[0]:
        return float('inf')
    else:
        return 1.0*(p1[1] - p2[1])/(p1[0] - p2[0])
def get_ccw(p1,p2,p3):
    return ((p2[0] - p1[0])*(p3[1] - p1[1])) - ((p2[1] - p1[1])*(p3[0] - p1[0]))

def distance(a,b):
    x1,y1 = a
    x2,y2 = b
    return ((x1-x2)**2 + (y1-y2)**2)

def rotating_calipers(h):
    hull_size = len(h)
    left_index = 0
    right_index = 0
    for i in range(hull_size):
        if h[left_index][0] > h[i][0]:
            left_index = i
        if h[right_index][0] < h[i][0]:
            right_index = i
    result = distance(h[left_index],h[right_index])
    max_idx = [left_index,right_index]
    for _ in range(hull_size):
        lp = h[left_index]
        rp = h[right_index]
        nlp = h[(left_index+1)%hull_size]
        nrp = h[(right_index+1)%hull_size]
        if get_ccw((0,0),(lp[0] - nlp[0],lp[1] - nlp[1]), (nrp[0] - rp[0],nrp[1]-rp[1])) > 0:
            left_index = (left_index+1)%hull_size
        else:
            right_index = (right_index+1)%hull_size
        if result < distance(h[left_index],h[right_index]):
            result =  distance(h[left_index],h[right_index])
            max_idx = [left_index,right_index]
    return result,[*h[max_idx[0]],*h[max_idx[1]]]

N = int(input())

points = [list(map(int,input().split())) for _ in range(N)]

points.sort(reverse=True)
start = points.pop()
points.sort(key= lambda p : (get_slope(p,start), p[1],p[0]))

hull = [start]

for point in points:
    hull.append(point)
    while len(hull)>2 and get_ccw(hull[-3],hull[-2],hull[-1])<=0:
        hull.pop(-2)
ffs = []

dis,r = rotating_calipers(hull)
print(dis)