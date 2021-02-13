N = int(input())
K = int(input())

if K:
    button_not = set(map(int,input().split()))
else:
    button_not = set()

allbutton = set(range(10))
possible_button = allbutton - button_not
down_num = 1000000
up_num = 1000000
min_result = abs(N-100)
for num in range(N,1000001):
    for k in str(num):
        if int(k) not in possible_button:
            break
    else:
        down_num = num
        break

for num in range(N,-1,-1):
    for k in str(num):
        if int(k) not in possible_button:
            break
    else:
        up_num = num
        break
if abs(up_num-N) <= abs(down_num-N):
    close_num = up_num
else:
    close_num = down_num
print(min(len(str(close_num))+abs(N-close_num),min_result))
