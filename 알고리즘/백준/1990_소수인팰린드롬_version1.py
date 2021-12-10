import sys

def input():
    return sys.stdin.readline().rstrip()
def check(N):
    
    for n in range(2,int(N**0.5)+1):
        if not N%n:
            return False
    return True
def make_palindrom(e):
    max_len = len(str(e))
    palind = [2,3,5,7]
    for zari in range(2,max_len+1):
        half_zari = zari//2
        for num in range(10**(half_zari-1),10**half_zari):
            if zari%2:
                for mid in range(10):
                    new_num = num*(10**(half_zari+1)) + mid*(10**half_zari) + int(str(num)[::-1])
                    palind.append(new_num)
            else:
                new_num = num*(10**half_zari) + int(str(num)[::-1])
                palind.append(new_num)
    return palind
a,b = map(int,input().split())




palind_drome = make_palindrom(b)

result = []
for num in palind_drome:
    if a<=num<=b:
        
        if check(num):
            result.append(num)
result.append(-1)
for row in result:
    print(row)