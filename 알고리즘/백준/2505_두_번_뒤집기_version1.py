import sys
def input():
    return sys.stdin.readline().rstrip()


def check(dire):
    if dire:
        po = [1,N+1,1]
        dire = 1
    else:
        po = [N,-1,-1]
        dire = -1
    cnt = 0
    copy_arr = arr[:]
    command = []
    while copy_arr != base_arr:
        if cnt == 2:
            return []
        flag = False
        start = -1
        ends = -1
        for ind in range(*po):
            if not flag and copy_arr[ind] != base_arr[ind]:
                flag = True
                start = ind
            elif flag and copy_arr[ind] == start:
                ends = ind
                break
        temp = (abs(ends-start)-1)//2+1
        for i in range(temp):
            copy_arr[start+i*dire],copy_arr[ends-dire*i] = copy_arr[ends-dire*i], copy_arr[start+i*dire]
        cnt += 1
        command.append(sorted([start,ends]))
    if len(command) == 1:
        command.append([1,1])
    return command
N = int(input())

arr = [0]+list(map(int,input().split()))
base_arr = list(range(N+1))
if arr == base_arr:
    print(1,1)
    print(1,1)
else:
    r1 = check(True)
    if not r1:
        r1 = check(False)
    for row in r1:
        print(*row)
    

