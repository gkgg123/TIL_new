import heapq

N = int(input())
rail_list = []
for idx in range(N):
    A,B = map(int,input().split())
    if A > B:
        A,B = B,A
    rail_list.append((A,B))
rail_list.sort(key=lambda x : x[1])

in_rail = []
d = int(input())
result = 0
for start,end in rail_list:
    if end-d <= start:
        heapq.heappush(in_rail,start)
    while in_rail and end-d > in_rail[0]:
        heapq.heappop(in_rail)
    result = max(result,len(in_rail))
print(result)
