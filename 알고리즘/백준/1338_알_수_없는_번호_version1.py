A,B = map(int,input().split())


if A>B:
    A,B = B,A

X,Y = map(int,input().split())
result = []
flag = True
if Y>=abs(X) or Y<0:
    flag = False
if flag:
    X = abs(X)
    value = X*(A//X)+Y
    while value<=B:
        if A<=value<=B:
            if result:
                flag = False
                break
            result.append(value)
        value += X
if flag and result:
    print(*result)
else:
    print('Unknwon Number')
