import sys
import heapq
input = sys.stdin.readline

def recommend(flag,heap):
    flag = -flag
    while heap and (heap[0][1]*flag not in problem_dict.keys() or problem_dict[heap[0][1]*flag] != heap[0][0]*flag):
        heapq.heappop(heap)
    result =heap[0]
    result = result[1]*flag
    return result

N = int(input())
max_heap = []
min_heap = []
problem_dict = {}
for _ in range(N):
    pb_num,l_num = map(int,input().split())
    max_heap.append((-l_num,-pb_num))
    min_heap.append((l_num,pb_num))

    problem_dict[pb_num] = l_num
heapq.heapify(max_heap)
heapq.heapify(min_heap)
M = int(input())

for _ in range(M):
    command,*arg = input().split()
    if command == 'add':
        pb_num,l_num = map(int,arg)
        heapq.heappush(max_heap,(-l_num,-pb_num))
        heapq.heappush(min_heap,(l_num,pb_num))
        problem_dict[pb_num] = l_num
    elif command == 'solved':
        pb_num = int(arg[0])
        del problem_dict[pb_num]
    else:
        flag = int(arg[0])
        if flag > 0:
            print(recommend(flag,max_heap))
        else:
            print(recommend(flag,min_heap))