import sys
import math
sys.setrecursionlimit(10005)
def input():
    return sys.stdin.readline().rstrip()

def shuffle(arr,cnt):
    arr = arr[N-2**cnt:] + arr[:N-2**cnt]
    cnt -= 1
    while cnt>=0:
        prev = 2**(cnt+1)
        move_arr = arr[:prev]
        fix_arr = arr[prev:]
        move = 2**cnt
        arr = move_arr[prev-move:] + move_arr[:prev-move] + fix_arr[:]
        cnt -= 1

    return arr
def solve():
    for one_k in range(1,max_K+1):
        shuffled = shuffle(list(range(1,N+1)),one_k)
        for two_k in range(1,max_K+1):
            shuffled = shuffle(shuffled[:],two_k)
            for ind in range(N):
                if shuffled[ind] != cards[ind]:
                    break
            else:
                print(one_k,two_k)
                return
N = int(input())

cards = list(map(int,input().split()))

max_K = 0
while 2**max_K<N:
    max_K += 1
max_K -= 1
solve()
