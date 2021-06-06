import sys


def input():
    return sys.stdin.readline().rstrip()

def choose_1(idx,val):
    global K
    if idx == line_cnt[0]:
        choose_2(0,0,val)
        return
    else:
        for i in range(K):
            choose_1(idx+1,val*10+number_list[i])
def check_length(val):
    val = str(val)
    return len(val)
def check_number(val):
    while val:
        if not number_visit[val%10]:
            return False
        val = val//10
    return True

def choose_2(idx,val,first_num):
    global K,result
    if idx == line_cnt[1]:
        last_num = first_num * val
        if check_length(last_num) == line_cnt[-1] and check_number(last_num):
            result += 1
        return
    else:
        for i in range(K):
            if check_length(first_num*number_list[i]) == line_cnt[idx+2] and check_number(first_num*number_list[i]):
                choose_2(idx+1,val*10+number_list[i],first_num)

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
result = 0
line_cnt = list(map(int,list_))
number_list = list(map(int,list__))
number_visit = [False for _ in range(10)]

for num in number_list:
    number_visit[num] = True


choose_1(0,0)

print(result)