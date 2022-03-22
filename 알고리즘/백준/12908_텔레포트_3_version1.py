import sys

def input():
    return sys.stdin.readline().rstrip()

def final(x,y):
    return abs(xe-x) + abs(ye-y)
def distance(A,B):
    x1,y1 = A
    x2,y2 = B
    return abs(x1-x2) + abs(y1-y2)
def dfs(position):
    x,y = position
    time = float('inf')
    
    for idx in range(3):
        if visited[idx]:
            visited[idx] = False
            A,B = teleport_dict[idx]
            time = min(time, dfs(A)+10 + distance(position,B))
            time = min(time,dfs(B)+10 + distance(position,A))
            visited[idx] = True
    time = min(time,final(x,y))
    return time
xs,ys = map(int,input().split())
xe,ye = map(int,input().split())

teleport_dict = []

for _ in range(3):
    x1,y1,x2,y2 = map(int,input().split())
    teleport_dict.append([(x1,y1),(x2,y2)])

result = abs(xs-xe) + abs(ys-ye)

visited = [True for _ in range(3)]


print(dfs((xs,ys)))