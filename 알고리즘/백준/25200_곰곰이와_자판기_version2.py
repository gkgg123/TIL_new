import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())


edges = []

for _ in range(M):
    x,y = map(int,input().split())
    edges.append((x,y))


result = [i for i in range(N+1)]


while edges:
    x,y = edges.pop()
    result[x] = result[y]

print(result[1:])