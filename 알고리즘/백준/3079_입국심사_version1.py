def check(number):
    remain_person = M

    for k in time_list:
        remain_person = remain_person - number//k
        if remain_person <=0:
            return -1
    return 1


N,M = map(int,input().split())
time_list = [int(input()) for _ in range(N)]

start = 1
end = ((M//N)+1)*max(time_list)
while start<end:
    mid = (start+end)//2
    remain_person = check(mid)

    if remain_person > 0:
        start = mid + 1
    else:
        end = mid -1
print(end)