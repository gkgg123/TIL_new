import heapq
import sys

input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    input_list = map(int,input().split())
    if i == 0 :
        for number in input_list:
            heapq.heappush(arr,number)
    else:
        for number in input_list:
            if number > arr[0]:
                heapq.heappushpop(arr,number)
big_list = heapq.nlargest(N,arr)
print(big_list[N-1])
