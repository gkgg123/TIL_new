import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()

N,K = map(int,input().split())

arr = list(map(int,input().split()))
current_index = [K+1 for _ in range(K+1)]
prev_index = [0 for _ in range(K+1)]
for index in range(K-1,-1,-1):
    # 현재 위치의 값이 나온 곳
    prev_index[index] = current_index[arr[index]]
    current_index[arr[index]] = index

multitap = set()
last_use = []
answer = 0
for index in range(K):
    if arr[index] not in multitap:
        if len(multitap) == N:
            answer += 1
            _,remove_num = heapq.heappop(last_use)
            multitap.remove(remove_num)
        multitap.add(arr[index])
    heapq.heappush(last_use, (-prev_index[index],arr[index]))

print(answer)