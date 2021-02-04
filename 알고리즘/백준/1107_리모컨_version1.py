# 1107 리모컨
def dfs(cnt,number):
    global min_result,N
    if cnt > 6:
        return
    else:
        if min_result == 0:
            return
        temp = abs(int(number) - N)+cnt
        if temp < min_result:
            min_result = temp
        for k in possible_button:
            dfs(cnt+1,number+str(k))




N = int(input())
K = int(input())
if K != 0:
    button_not = set(map(int,input().split()))
else:
    button_not = set()
allbutton = set(range(10))
possible_button = allbutton - button_not
min_result = abs(N-100)

for i in possible_button:
    dfs(1,str(i))
print(min_result)