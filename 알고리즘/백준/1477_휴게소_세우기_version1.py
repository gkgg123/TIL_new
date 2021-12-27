import sys

def input():
    return sys.stdin.readline().rstrip()
def check(s):
    count = 0

    for i in range(1,N+2):
        count += (rest_area[i] - rest_area[i-1]-1)//s
    if count > M:
        return False
    return True
N,M,L = map(int,input().split())

rest_area = [0]+list(map(int,input().split()))+[L]
rest_area.sort()
left = 0
right = L

while left+1 < right:
    mid = (left+right)//2

    if check(mid):
        right = mid
    else:
        left = mid


print(right)