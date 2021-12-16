import sys
def input():
    return sys.stdin.readline().rstrip()
def check(box_number):
    count = 0
    for st,ed,gap in rules:
        copy_box = box_number
        if copy_box>=st:
            copy_box = min(copy_box,ed)
            count = count + (copy_box-st)//gap + 1
    
    if count >= D:
        return True
    return False

N,K,D = map(int,input().split())

rules = []

for _ in range(K):
    x,y,gap = map(int,input().split())
    rules.append((x,y,gap))
left = 1
right = N

while left+1<right:
    mid = (left+right)//2

    if check(mid):
        right = mid
    else:
        left = mid
print(right)