
def gcd(a,b):
    if (a%b==0):
        return b
    else:
        return gcd(b,a%b)


N = int(input())
arr =list(map(int,input().split()))

arr.sort()

left_side = [0]*N
right_side = [0]*N
left_idx = 0
right_idx = 1
left_side[0] = arr[0]
right_side[-1] = arr[-right_idx]
for _ in range(N-1):
    left_gcd = gcd(left_side[left_idx],arr[left_idx+1])
    right_gcd = gcd(right_side[-right_idx],arr[-(right_idx+1)])
    left_side[(left_idx+1)] = left_gcd
    right_side[-(right_idx+1)] = right_gcd
    left_idx += 1
    right_idx += 1
result_gcd = -1
remove_data = -1
for i in range(N):
    remove_value = arr[i]
    if i == 0 or i == N-1:
        if i == 0:
            total_gcd = right_side[1]
        else:
            total_gcd = left_side[-2]
        if remove_value%total_gcd:
            if result_gcd < total_gcd:
                result_gcd = total_gcd
                remove_data = remove_value
    else:
        left_gcd = left_side[i-1]
        right_gcd = right_side[i+1]
        total_gcd = gcd(left_gcd,right_gcd)
        if remove_value%total_gcd:
            if result_gcd < total_gcd:
                result_gcd = total_gcd
                remove_data = remove_value

if result_gcd == -1:
    print(result_gcd)
else:
    print(result_gcd,remove_data)


