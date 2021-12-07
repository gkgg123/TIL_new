import sys
def input():
    return sys.stdin.readline().rstrip()


G = int(input())



left = 1
right = 2
ans = []
while left<right:
    mG = right**2 - left**2

    if mG<G:
        right += 1
    elif mG == G:
        ans.append(right)
        left += 1
    else:
        left += 1
    if right - left >G:
        break
if ans:
    for row in ans:
        print(row)
else:
    print(-1)
