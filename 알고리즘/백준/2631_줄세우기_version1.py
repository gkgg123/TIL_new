# 2631 줄 세우기
# LIS의 길이를 구하기 위한 방법 복잡도 O(Nlogn)로 구하기 
N = int(input())
arr = list(int(input()) for _ in range(N))
LIS = []
LIS.append(arr[0])
temp = 0
for number in arr[1:]:
    for ind,val in enumerate(LIS):
        if number > val and number not in LIS:
            temp = number
        elif number < val and number not in LIS:
            LIS[ind] = number
            temp = 0
    if temp:
        LIS.append(temp)
    temp = 0
print(N-len(LIS))
    

