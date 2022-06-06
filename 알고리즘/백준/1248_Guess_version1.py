import sys

def input():
    return sys.stdin.readline().rstrip()

def check(num,idx,gap):
    if num> 0 and st[idx+gap] == '+':
        return True
    if num<0 and st[idx+gap] == '-':
        return True
    if num == 0 and st[idx+gap] == '0':
        return True
    return False

def sol(idx,po,len):
    if po == -1:
        print(*arr)
        exit()
        return
    cur = st[idx]
    if cur == '+':
        for cur_num in range(1,11):
            for gap in range(N-po):
                temp = sum(arr[po:po+gap+1])
                if not check(temp+cur_num,idx,gap):
                    break
            else:
                arr[po] = cur_num
                sol(idx-(len+1),po-1,len+1)
                arr[po] = 0
                    
    elif cur == '-':
        for cur_num in range(-1,-11,-1):
            for gap in range(N-po):
                temp = sum(arr[po:po+gap+1])
                if not check(temp+cur_num,idx,gap):
                    break
            else:
                arr[po] = cur_num
                sol(idx-(len+1),po-1,len+1)
                arr[po] = 0
    else:
        arr[po] = 0
        sol(idx-(len+1),po-1,len+1)

N = int(input())

st = list(input())

arr = [0 for _ in range(N)]


sol((N+1)*N//2-1,N-1,1)