import sys

def input():
    return sys.stdin.readline().rstrip()

def check(mid):
    set_list = set()
    for y in range(M):
        temp = arr[y][mid:]
        if temp in set_list:
            return False
        else:
            set_list.add(temp)
    return True

N,M = map(int,input().split())


arr = ['' for _ in range(M)]

for _ in range(N):
    input_string = input()
    for y in range(M):
        arr[y] += input_string[y]

left = -1
right = N

while left+1 < right:
    mid = (left + right)//2


    if check(mid):
        left = mid
    else:
        right = mid
print(left)