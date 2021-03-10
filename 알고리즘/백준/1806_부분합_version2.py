i=input;N,L = map(int,i().split());R=list(map(int,i().split()));INF=float('inf');S,E,T=0,0,0;A=INF
while True:
    if T>=L:A=min(A,E-S);T-=R[S];S+=1
    elif E == N:break
    else:T+=R[E];E+=1
print(0 if A == INF else A)