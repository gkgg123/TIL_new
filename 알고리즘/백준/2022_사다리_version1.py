x,y,c = map(float,input().split())

right = min(x,y)
left = 0
answer = 0
for _ in range(10000):
    mid = (left+right)/2

    w1 = (x**2 - mid**2)**0.5
    w2 = (y**2 - mid**2)**0.5
    cal = (w1*w2)/(w1+w2)
    if cal >= c:
        left = mid
        answer = mid
    else:
        right = mid
print(answer)