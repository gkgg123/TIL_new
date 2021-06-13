# xiaowuc1님 풀이
import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

pay_list = {}

for _ in range(N):
    name,pay = input().split()
    pay_list[name] = int(pay)



recipe_list = [input() for _ in range(M)]


while True:
    flag = False

    for recipes in recipe_list:
        complete_name,others = recipes.split('=')
        other_list = others.split('+')
        temp_sum = 0
        for other in other_list:
            cnt = int(other[0])
            name = other[1:]
            if pay_list.get(name):
                temp_sum += cnt*pay_list[name]
            else:
                temp_sum = -1
                break
        if temp_sum<0:
            continue
        if complete_name not in pay_list or pay_list[complete_name]>temp_sum:
            pay_list[complete_name] = temp_sum
            flag = True
    if not flag:
        break

if pay_list.get('LOVE'):
    print(min(pay_list['LOVE'],1000000001))
else:
    print(-1)