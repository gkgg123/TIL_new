def ccw(start,second,third):
    vector1 = [second[0]-start[0],second[1]-start[1]]
    vector2 = [third[0]-start[0],third[1]-start[1]]
    outer = vector1[0]*vector2[1] - vector2[0]*vector1[1]
    if outer < 0:
        print(-1)
    elif not outer:
        print(0)
    else:
        print(1)


P1 = list(map(int,input().split()))
P2 = list(map(int,input().split()))
P3 = list(map(int,input().split()))


ccw(P1,P2,P3)

# https://gaussian37.github.io/math-algorithm-ccw/