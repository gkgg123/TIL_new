import sys

def input():
    return sys.stdin.readline().rstrip()



N = int(input())
A = list(map(int,input().split()))
dict_A = {}
for k in range(N):
    dict_A[A[k]] = k

B = list(map(int,input().split()))
convert_B = [0]*N
for ind,k in enumerate(B):
    convert_B[ind] = dict_A[k]
LIS = [convert_B[0]]



for ind in range(1,N):
    if convert_B[ind] > LIS[-1]:
        LIS.append(convert_B[ind])
    else:
        left = -1
        right = len(LIS)
        while left + 1 < right:
            mid = (left + right)//2

            if LIS[mid] >= convert_B[ind]:
                right = mid
            else:
                left = mid
        LIS[right] = convert_B[ind]

print(len(LIS)) 