import sys
import heapq
def input():
    return sys.stdin.readline().rstrip()



N = int(input())

arr = [list(map(int,input().split())) for _ in range(N)]
INF = float('inf')

arr.sort()
arr.append((INF,INF))
answer = 0
start_point = arr[0][0]
end_point = arr[0][1]
for i in range(N+1):
    if end_point >= arr[i][0]:
        end_point = max(arr[i][1],end_point)
        continue
    else:
        answer = answer + (end_point-start_point)
        start_point = arr[i][0]
        end_point = arr[i][1]

print(answer)