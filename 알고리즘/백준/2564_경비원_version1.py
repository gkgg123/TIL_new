M,N = map(int,input().split())
S = int(input())
# 북쪽 1 ==>0
# 남쪽 2 ==>N-1
# 서쪽 3 =>0
# 동쪽 4 => N-1
input_list = []
total_length = (N+M)*2
for tc in range(S+1):
    n1,n2 = map(int,input().split())
    if n1 == 1:
        input_list.append(n2)
    elif n1 == 2:
        input_list.append(M+N+(M-n2))
    elif n1 == 3:
        input_list.append(2*M+N+(N-n2))
    else:
        input_list.append(M+n2)

patrol = input_list[-1]
result = 0


for idx in range(S):
    temp = abs(input_list[idx]-patrol)
    result += min(temp,total_length-temp)
print(result) 