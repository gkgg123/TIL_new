import sys

input = sys.stdin.readline

N = int(input())


bit_cnt_list = [0]*1024
for _ in range(N):
    num = input().strip()
    temp = 0
    for bit_num in num:
        temp = temp | 2**(int(bit_num))
    bit_cnt_list[temp] += 1
result = 0
for k in range(1,1024):
    for t in range(k,1024):
        if k == t:
            if bit_cnt_list[k] >= 2:
                result = result + (bit_cnt_list[k]*(bit_cnt_list[k]-1))//2
        else:
            if bit_cnt_list[k] != 0 or bit_cnt_list[t] != 0:
                if k&t >0:
                    result = result + bit_cnt_list[k]*bit_cnt_list[t]

print(result)
