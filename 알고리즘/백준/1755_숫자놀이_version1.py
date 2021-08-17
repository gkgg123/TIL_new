M,N = map(int,input().split())
def string_fun(num):
    temp = []
    for st in num:
        temp.append(num_st[int(st)])
    return ''.join(temp)
arr = []
for num in range(M,N+1):
    arr.append(str(num))

num_st = ['zero','one','two','three','four','five','six','seven','eight','nine']
arr.sort(key=string_fun)


for i in range(len(arr)//10):
    print(*arr[i*10:(i+1)*10])

if len(arr)%10:
    for i in range(len(arr)-len(arr)%10,len(arr)):
        print(arr[i],end=' ')