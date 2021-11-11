import sys

def input():
    return sys.stdin.readline().rstrip()


def distance(p1,p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    return x*x + y*y
N = int(input())

points = []
for _ in range(N):
    x,y = map(int,input().split())
    points.append((x,y))

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
    result = min(result,left_distance[idx]**0.5 + right_distance[idx+1]**0.5)
print(result)
