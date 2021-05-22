def get_prim_number(N):
    prime_check = [True]*(N+1)
    prime_check[0] = False
    prime_check[1] = True
    result = []

    for num in range(2,N+1):
        if prime_check[num]:
            result.append(num)
            for new_num in range(num*2,N+1,num):
                prime_check[new_num] = False
    
    return result


N = int(input())

prime_list = get_prim_number(N)
prefix_sum = prime_list[:]
for i in range(len(prime_list)-1):
    prefix_sum[i+1] += prefix_sum[i]

prefix_sum = [0] + prefix_sum


cnt = 0
left = 0
right = 0
while right <len(prefix_sum):
    temp = prefix_sum[right] - prefix_sum[left]

    if temp == N:
        cnt += 1
        right += 1
    elif temp < N:
        right += 1
    else:
        left += 1
        if temp == 0:
            left = right

print(cnt)