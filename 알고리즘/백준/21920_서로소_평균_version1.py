def get_divide_list(num):
    result = []
    for i in range(1,int(num**0.5)+1):
        if not num%i:
            result.extend([i,num//i])

    result = list(set(result))
    result.remove(1)
    return result

N = int(input())

arr = list(map(int,input().split()))

X = int(input())


X_list = get_divide_list(X)

answer = 0
cnt = 0
for num in arr:
    for x_num in X_list:
        if not num%x_num:
            break
    else:
        answer += num
        cnt += 1

print(answer/cnt)