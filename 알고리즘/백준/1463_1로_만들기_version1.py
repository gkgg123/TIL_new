a= int(input())
def cal(a):
    temp = []
    for i in a:
        temp.append(i-1)
        if i%3==0:
            temp.append(i/3)
        if i%2==0:
            temp.append(i/2)
    return temp
cnt=0
minimum=[a]
while True:
    if a==1:
        print(cnt)
        break
    temp=minimum[:]
    minimum=[]
    minimum=cal(temp)
    cnt+=1
    if min(minimum)==1:
        print(cnt)
        break