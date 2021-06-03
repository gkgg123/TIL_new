import sys
import heapq
input = sys.stdin.readline
N = int(input())
time_list = []
for i in range(N):
    start_time,end_time = map(int,input().split())
    heapq.heappush(time_list,(start_time,i))
    heapq.heappush(time_list,(end_time,i))
isSeatperson = [-1]*N
seat_info = []
com_idx = 0
min_com_list = []

while time_list:
    _,person_number = heapq.heappop(time_list)

    if isSeatperson[person_number] == -1:
        if min_com_list:
            isSeatperson[person_number] = heapq.heappop(min_com_list)
        else:
            isSeatperson[person_number] = com_idx
            com_idx += 1
    else:
        heapq.heappush(min_com_list,isSeatperson[person_number])
        seat_info.append(isSeatperson[person_number])


max_com = max(seat_info)+1

result = [0]*max_com

for com_number in seat_info:
    result[com_number] += 1

print(max_com)
print(*result)