N,M = map(int,input().split())

arr = [list(map(int,list(input()))) for _ in range(N)]
result = 0
# 0은 가로인걸로 1은 세로인걸로 판별
for bit_shape in range(2**(N*M)):
    total_sum = 0
    for x in range(N):
        sub_sum = 0 # 작은 단위의 SUM
        for y in range(M):
            idx = x*M + y
            if not bit_shape & (1<<idx):
                sub_sum = sub_sum*10 + arr[x][y]
            else:
                total_sum += sub_sum
                sub_sum = 0
        total_sum += sub_sum
    
    for y in range(M):
        sub_sum = 0
        for x in range(N):
            idx = x*M + y
            if bit_shape & (1<<idx):
                sub_sum = sub_sum*10 + arr[x][y]
            else:
                total_sum += sub_sum
                sub_sum = 0
        total_sum += sub_sum
    result = max(result,total_sum)
print(result)

        
