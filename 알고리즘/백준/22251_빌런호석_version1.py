import sys

def input():
    return sys.stdin.readline().rstrip()
def init():
    for num in range(10):
        for other_num in range(num+1,10):
            xor_cnt = bin(numbers[num]^numbers[other_num]).count('1')
            reverse_table[num][other_num] = xor_cnt
            reverse_table[other_num][num] = xor_cnt
           

N,K,P,X = map(int,input().split())
numbers = [
0b1111110,
0b0110000,
0b1101101,
0b1111001,
0b0110011,
0b1011011,
0b1011111,
0b1110000,
0b1111111,
0b1111011]
reverse_table = [[0 for _ in range(10)] for _ in range(10)]
init()
result = 0
for num in range(1,N+1):
    reverse_cnt = 0
    copy_X = X

    for digit in range(K):
        reverse_cnt += reverse_table[copy_X%10][num%10]
        copy_X//=10
        num//=10
    
    if 1<=reverse_cnt<=P:
        result += 1
print(result)