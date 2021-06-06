import sys
from itertools import product
def input():
    return sys.stdin.readline().rstrip()

def dfs(first_num,idx,total):
    global result
    if idx == line_cnt[1]:
        str_total = str(total)
        str_set = set(str_total)
        if len(str_total) == line_cnt[idx+2] and not (str_set-total_num):
            result += 1
    else:
        for k in int_total_num:
            temp = k*first_num
            str_temp = str(temp)
            str_set = set(str_temp)
            if len(str_temp) == line_cnt[idx+2] and not (str_set-total_num):
                number_of_digit = 10**idx
                temp_num = temp * number_of_digit
                dfs(first_num,idx+1,total+temp_num)


N = int(input())
list_ = input().split()

K = input()
list__ = input().split()

if len(K) == 0:
    K = int(list_[N])
    list__ = list_[N + 1 : ]
    list_  = list_[ : N]
else:
    K = int(K)
line_cnt = list(map(int,list_))
number_list = list__[:]
total_num = set(number_list)
int_total_num = set(map(int,number_list))
result = 0
for num_line1 in product(number_list,repeat=line_cnt[0]):
    first_line_num = int(''.join(num_line1))
    dfs(first_line_num,0,0)


print(result)