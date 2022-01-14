import sys
from bisect import bisect_left,insort

def input():
    return sys.stdin.readline().rstrip()

def find_idx(key):
    right_ind = bisect_left(key_list,key)
    if right_ind == len(key_list):
        right_abs = INF
    else:
        right_abs =  abs(key - key_list[right_ind])
    if right_ind-1>=0:
        left_abs = abs(key_list[right_ind-1] - key) 
    else:
        left_abs = INF
    if right_abs>K and left_abs>K:
        return INF
    if right_abs == left_abs:
        return -1
    if right_abs<left_abs:
        return right_ind
    return right_ind-1


N,M,K = map(int,input().split())
INF = float('inf')
JBNU = {}
key_list = []
for _ in range(N):
    x,y = map(int,input().split())
    JBNU[x] = y
    insort(key_list,x)



for _ in range(M):
    command, *arg= map(int,input().split())

    if command == 1:
        key,value = arg
        insort(key_list,key)
        JBNU[key] = value
    elif command == 2:
        key,value = arg
        if JBNU.get(key):
            JBNU[key] = value
        else:
            ind = find_idx(key)
            if ind == INF or ind == -1:
                continue
            JBNU[key_list[ind]] = value

    else:
        key = arg[0]
        if JBNU.get(key):
            print(JBNU[key])
        else:
            ind = find_idx(key)

            if ind == INF:
                print(-1)
            elif ind == -1:
                print('?')
            else:
                print(JBNU[key_list[ind]])


            
