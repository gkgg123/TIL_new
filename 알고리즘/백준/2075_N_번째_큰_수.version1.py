import heapq
import sys

input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    temp = list(map(int,input().split()))
    for number in temp:
        heapq.heappush(arr,number)
    while len(arr) > N:
        heapq.heappop(arr)



result = heapq.heappop(arr)
print(result)
