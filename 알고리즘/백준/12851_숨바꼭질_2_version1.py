# 12851 숨바꼭질

N,M = map(int,input().split())
dp = [-1]*100001
if M != N:
    stack = [(N,0,'')]
    flag = False
    result = float('inf')
    dire = ['M','P','T']
    total = set()
    visited = set()
    while stack:
        X,time,how = stack.pop(0)
        if time > result:
            break
        temp =  [X-1,X+1,X*2]
        for ind,k in enumerate(temp):
            if 0<=k<=100000 and time+1<=result:
                if dp[k] == -1 or dp[k] == time+1:
                    dp[k] = time+1
                    stack.append((k,time+1,how+dire[ind]))
                    if k == M:
                        result = time+1
                        total.add(how+dire[ind])

        
    print(result)
    print(len(total))
else:
    print(0)
    print(1)