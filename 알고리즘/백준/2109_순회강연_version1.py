import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

arr = []

for _ in range(N):
    pay,day = map(int,input().split())
    arr.append((day,-pay))

heapq.heapify(arr)


result = 0
visited = []
while arr:
    day,pay = heapq.heappop(arr)
    heapq.heappush(visited,-pay)
    if len(visited) > day:
        heapq.heappop(visited)
print(sum(visited))
