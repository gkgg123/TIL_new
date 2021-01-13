T=int(input())

for t in range(T):
    n,m=map(int,input().split(' '))
    k=m-n
    n_result=1
    m_result=1
    k_result=1
    for i in range(1,m+1):
        m_result*=i
    for j in range(1,n+1):
        n_result*=j
    for p in range(1,k+1):
        k_result*=p
    print(int(m_result/(n_result*k_result)))
        