import heapq
def check(D):
    global result
    possible_set = []

    while rail_list:
        END,START = heapq.heappop(rail_list)
        if END-D <=START:
            heapq.heappush(possible_set,START)
        while possible_set and possible_set[0] < END-D:
            heapq.heappop(possible_set)
        
        result = max(result,len(possible_set))




N = int(input())
rail_list = []
for idx in range(N):
    A,B = map(int,input().split())
    if A > B:
        A,B = B,A
    heapq.heappush(rail_list,(B,A))

d = int(input())
result = 0
check(d)
print(result)
