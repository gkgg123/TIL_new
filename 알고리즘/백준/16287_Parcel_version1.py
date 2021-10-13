import sys
def solution():
    for ind1 in range(N-1):
        if ind1>=2:
            for ind2 in range(ind1+1,N):
                temp = arr[ind1] + arr[ind2]
                if temp >= W:continue
                if W-temp>=400000:continue
                if weight_list[W-temp]:
                    return 'YES'
        
        for ind3 in range(ind1):
            temp = arr[ind1] + arr[ind3]
            if temp>=W:continue
            weight_list[temp] = True
    return 'NO'
def input():
    return sys.stdin.readline().rstrip()

W,N = map(int,input().split())


arr = list(map(int,input().split()))

arr.sort()
weight_list = [False for _ in range(W+1)]

print(solution())
