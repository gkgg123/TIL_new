import heapq
import sys
import random
def shuffle(a):
    n = len(a)
    for i in range(n-1):
        j = random.randint(i, n-1)
        (a[i], a[j]) = (a[j], a[i])
    return a
def input():
    return sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int,input().split()))

arr.sort()
result = 0
for i in range(2001):
    node_list = []
    heapq.heappush(node_list,0)
    heapq.heappush(node_list,0)
    heapq.heappush(node_list,0)
    for ham in arr:
        cur = heapq.heappop(node_list)
        heapq.heappush(node_list,cur+ham)
    arr = shuffle(arr)
    result = max(result,node_list[0])
print(result)