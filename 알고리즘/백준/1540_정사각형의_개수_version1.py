import sys

def input():
    return sys.stdin.readline().rstrip()


N = int(input())
if N <4:
    print(0)
else:
    min_len = int(N**0.5)
    answer = 0
    for i in range(1,min_len):
        answer += i*i

    N -= min_len*min_len
    
    while N:
        
        for i in range(1,min(min_len,N)):
            answer += i

        N = max(N-min_len,0)
    print(answer)
        