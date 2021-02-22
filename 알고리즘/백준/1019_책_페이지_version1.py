def calc(n,t):

    cnt = 1
    while n!=0:
        while n%10 != 9:
            if n!=0:
                for i in str(n):
                    s_i[int(i)] += cnt
                n-=1
            else:
                return
        if n<10:
            for i in range(n+1):
                s_i[i]+=cnt
            s_i[0]-=cnt
            return
        else:
            for i in range(10):
                s_i[i]+=(n//10+1)*cnt
        s_i[0] -= cnt
        cnt *= 10
        n=n // 10
    return


N=int(input())
s_i=[0]*10
calc(N,s_i)
print(*s_i)