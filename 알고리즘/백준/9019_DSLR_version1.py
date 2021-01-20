# # # 9019 DSLR 
# # # 레지스터 0이상 10000미만 십진수 저장
# # # n = ((d1 × 10 + d2) × 10 + d3) × 10 + d4
# # # D는 n을 두배로 바꾼다. 결과값이 9999보다 큰 경우는 1만으로 나눈 값 (2n mod 10000)
# # # S : n에서 1을 뺀값 n이 0이면 9999로 대신 저장
# # # L : n을 각자리숫를 왼편으로 회전시켜 그 결과를 레지스터에 저장한다.  d2, d3, d4, d1
# # # R : n을 오른쪽으로 회전 
import collections

def DSLR(num):
    D_num = num *2
    if D_num > 9999:
        D_num = D_num%10000
    S_num = num -1
    if not num:
        S_num = 9999
    L_num = (num*10)%10000 + num//1000
    R_num = num//10 + num%10*1000
    return [D_num,S_num,L_num,R_num]



T = int(input())
DSLR_IND = ['D','S','L','R']
for tc in range(T):
    A,B = list(map(int,input().split()))
    deque = collections.deque()
    deque.append((A,''))
    dp = [0]*10000
    dp[A] = 1
    flag = False
    while deque:
        num,result = deque.popleft()
        if num == B:
            break
        temp = DSLR(num)
        for ind in range(4):
            if not dp[temp[ind]]:
                dp[temp[ind]] = 1
                if temp[ind] == B:
                    result = result + DSLR_IND[ind]
                    flag = True
                    break
                deque.append((temp[ind],result+DSLR_IND[ind]))
        if flag:
            break
    print(result)
