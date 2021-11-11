import sys

def input():
    return sys.stdin.readline().rstrip()

class Point():
    def __init__(self,x,y) -> None:
        self.x = x
        self.y = y
def distance(p1,p2):
    return ((p1.x - p2.x)**2 + (p1.y - p2.y)**2)**0.5
N = int(input())

points = []
for _ in range(N):
    x,y = map(int,input().split())
    points.append(Point(x,y))

left_idx = 0
right_idx = 0

for i in range(N-1):
    for j in range(i+1,N):
        if distance(points[i],points[j]) > distance(points[left_idx],points[right_idx]):
            left_idx = i
            right_idx = j

left_point = points[left_idx]
right_point = points[right_idx]
points.sort(key = lambda p : distance(p,left_point))


left_distance = [ 0 for _ in range(N)]
right_distance = [0 for _ in range(N)]

for idx in range(N):
    if idx:
        left_distance[idx] = left_distance[idx-1]
    for left_idx in range(idx):
        left_distance[idx] = max(left_distance[idx], distance(points[idx],points[left_idx]))

for idx in range(N-1,-1,-1):
    if idx != N-1:
        right_distance[idx] = right_distance[idx+1]
    for right_idx in range(idx+1,N):
        right_distance[idx] = max(right_distance[idx], distance(points[idx],points[right_idx]))

result = float('inf')
for idx in range(N-1):
    result = min(result,left_distance[idx] + right_distance[idx+1])
print(result)
