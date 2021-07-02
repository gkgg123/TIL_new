import sys

def input():
    return sys.stdin.readline().rstrip()

def replaceNumber(k):
    if k.islower():
        num = (ord(k) - ord('a')+1)*2
    else:
        num = (ord(k)-ord('A'))*2+1
    return num



N  = int(input())
result = []

for _ in range(N):
    TC = list(input())
    temp = ''
    tc_temp = []
    for k in TC:
        if k.isdigit():
            temp += k
        else:
            if temp:
                tc_temp.append([0,int(temp),len(temp)])
                temp = ''
            tc_temp.append([1,replaceNumber(k)])
    if temp:
        tc_temp.append([0,int(temp),len(temp)])
    
    result.append([tc_temp,''.join(TC)])
    

result.sort()

for row in result:
    print(row[1])
