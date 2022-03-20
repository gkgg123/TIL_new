import sys
from heapq import heappop,heapify
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

heap = []

for i in range(N):
    s,e = map(int,input().split())
    heap.append((s,e))

heapify(heap)

S,E = heappop(heap)
answer = E-S
while heap:
    new_S , new_E = heappop(heap)

    if new_S>=S and new_E<=E:
        continue
    elif S<=new_S<=E and new_E>E:
        answer += new_E-E
    else:
        answer += new_E-new_S

    S = new_S
    E = new_E

print(answer)