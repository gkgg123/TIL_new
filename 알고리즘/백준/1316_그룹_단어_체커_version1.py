T=int(input())
cnt=0
for test_case in range(T):
    sp=list(input())
    total=[]
    for i,v in enumerate(sp):
        if i!=len(sp)-1:
            if sp[i]!=sp[i+1]:
                total.append(sp[i])
        else:
            total.append(sp[i])
    for k in total:
        if total.count(k)>1:
            break
    else:
        cnt=cnt+1
print(cnt)
