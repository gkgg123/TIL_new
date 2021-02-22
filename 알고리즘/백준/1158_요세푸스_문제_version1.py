N,K=map(int,input().split(' '))
result=[]
temp=K-1
first=list(range(1,N+1))
for i in range(N):
    if temp < len(first):
        result.append(first.pop(temp))
        temp+=K-1
    else:
        temp=temp%len(first)
        result.append(first.pop(temp))
        temp+=K-1
print('<',end='')
for k in result:
    if k==result[-1]:
        print(k,end='')
    else:
        print(k,end=', ')
print('>')