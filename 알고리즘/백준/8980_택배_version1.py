import sys

def input():
    return sys.stdin.readline().rstrip()


N,C = map(int,input().split())
M = int(input())

capacity = [0 for _ in range(N+1)]

arr = [list(map(int,input().split())) for _ in range(M)]


arr.sort(key= lambda x : (x[1],x[0],-x[2]))


result = 0
for ind in range(M):
    left,right,curBoxCnt = arr[ind]
    inMemoryCnt = 0
    for node in range(left,right):
        inMemoryCnt = max(inMemoryCnt,capacity[node])

    addBoxCnt = min(curBoxCnt,C - inMemoryCnt)


    for node in range(left,right):
        capacity[node] += addBoxCnt
    result += addBoxCnt
print(result)