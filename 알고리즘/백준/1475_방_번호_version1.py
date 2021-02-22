import math
a=input()
k={}
for i in range(10):
    k[i]=0
for j in a:
    j=int(j)
    k[j]+=1
result1=0
result2=0
for index,value in k.items():
    if index==6 or index==9:
        result2=k[9]+k[6]
    else:
        if result1<value:
            result1=value
            

result2=math.ceil(result2/2)
if result2>result1:
    print(result2)
else:
    print(result1)