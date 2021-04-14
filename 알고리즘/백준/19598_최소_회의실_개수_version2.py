N = int(input())

metting = []
for _ in range(N):
    start,end = map(int,input().split())
    metting.append([start,1])
    metting.append([end,-1])
metting.sort()
result = 0
metting_cnt = 0 
for _,state in metting:
    metting_cnt += state
    result = max(metting_cnt,result)
print(result)