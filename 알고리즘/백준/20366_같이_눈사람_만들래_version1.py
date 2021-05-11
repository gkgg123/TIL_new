N = int(input())

arr = list(map(int,input().split()))

arr.sort()


elsa_start = 0
elsa_end = N -1
result = float('inf')

for elsa_start in range(N-3):
    for elsa_end in range(elsa_start+3,N):
        anna_start = elsa_start + 1
        anna_end = elsa_end - 1
        elsa = arr[elsa_start] + arr[elsa_end]
        while anna_start < anna_end:
            anna = arr[anna_start] + arr[anna_end]
            temp = elsa-anna
            if result > abs(temp):
                result = abs(temp)
            
            if temp > 0:
                anna_start += 1
            else:
                anna_end -= 1



print(result)