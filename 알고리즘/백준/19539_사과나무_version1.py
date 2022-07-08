import sys

def input():
    return sys.stdin.readline().rstrip()

def solve():
    if sum(ends)%3:
        return 'NO'
    cnt2 = 0
    for num in ends:
        cnt2 += num//2
    if cnt2>=sum(ends)//3:
        return 'YES'
    return 'NO'


N = int(input())
ends = list(map(int,input().split()))
print(solve())
