import sys
import heapq

input = sys.stdin.readline


N, K = map(int,input().split())

visited = [False]*K
jewel = []
for _ in range(N):
    m,v = map(int,input().split())
    heapq.heappush(jewel,(m,v))

bags = []
for _ in range(K):
    bags.append(int(input()))

bags.sort()
result = 0
possible_jewel = []
for bag in bags:
    while jewel and jewel[0][0] <= bag:
        m,v = heapq.heappop(jewel)
        heapq.heappush(possible_jewel,-v)
    
    if possible_jewel:
        result -= heapq.heappop(possible_jewel)
        
    

print(result)