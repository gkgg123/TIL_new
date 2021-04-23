
# skrud3021 님 코드 공부한거
N = int(input())

A,B,C,D = [],[],[],[]


for _ in range(N):
    a,b,c,d = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)


ab_sum = [i+j for i in A for j in B]
ab_sum.sort()
ab_sum.append(2<<29+1)
cd_sum = [i+j for i in C for j in D]
cd_sum.sort(reverse=True)
cd_sum.append(2<<29+1)
ab_ind = 0
cd_ind = 0
result = 0
while ab_ind <N**2 and cd_ind<N**2:
    sum_mid = ab_sum[ab_ind] + cd_sum[cd_ind]
    if sum_mid > 0:
        cd_ind += 1
    elif sum_mid < 0:
        ab_ind += 1
    else:
        ab_start_ind = ab_ind
        cd_start_ind = cd_ind
        ab_value = ab_sum[ab_ind]
        cd_value = cd_sum[cd_ind]
        while ab_value == ab_sum[ab_ind]:
            ab_ind += 1
        while cd_value == cd_sum[cd_ind]:
            cd_ind += 1
        
        result = result + (ab_ind-ab_start_ind)*(cd_ind-cd_start_ind)

print(result)