# 1697 숨바꼭질

#  수빈이는 N 동생은 K 
#  수빈이는 X-1 or X+1 2*X


N,M = map(int,input().split())

result = 0
stack = [(N,0)]
visited = [0]*100001
while stack:
    cu_n,cnt = stack.pop(0)
    if cu_n == M:
        break
    if 0<= cu_n <= 100000:
        if 0<= cu_n -1 <= 100000:
            if not visited[cu_n-1]:
                visited[cu_n-1] =1
                stack.append((cu_n-1,cnt+1))
        if 0<= cu_n+1 <= 100000:
            if not visited[cu_n+1]:
                visited[cu_n+1] =1
                stack.append((cu_n+1,cnt+1))
        if 0<= cu_n*2 <= 100000:
            if not visited[cu_n*2]:
                visited[cu_n*2] =1
                stack.append((cu_n*2,cnt+1))
print(cnt)