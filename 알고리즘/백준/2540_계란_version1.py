import sys


def input():
    return sys.stdin.readline().rstrip()

def pick_eggs(D):
    global min_value,result
    total_set = set(range(4))
    total_set.remove(D)
    copy_eggs = [row for row in eggs]
    A,B,C = sorted(list(total_set),key= lambda x : eggs[x])
    temp = []
    count = 0
    if (copy_eggs[A] + copy_eggs[B] + copy_eggs[C])%2:
        if copy_eggs[C] and copy_eggs[D]:
            copy_eggs[C] -= 1
            copy_eggs[D] -= 1
            copy_eggs[B] += 2
            temp.append(copy_eggs[:])
            count += 1
    A,B,C = sorted(list(total_set),key= lambda x : copy_eggs[x])
    if not (copy_eggs[A] + copy_eggs[B] >= copy_eggs[C]):
        while copy_eggs[B] == 0 and copy_eggs[C] >= 2:
            if copy_eggs[D] <=0:
                return
            for _ in range(2):
                copy_eggs[C] -= 1
                copy_eggs[D] -= 1
                copy_eggs[B] += 2
                count += 1
                temp.append(copy_eggs[:])
            A,B,C = sorted(list(total_set),key= lambda x : copy_eggs[x])
        while copy_eggs[A] + copy_eggs[B] < copy_eggs[C] and copy_eggs[C]:
            copy_eggs[C] -= 1
            copy_eggs[B] -= 1
            copy_eggs[A] += 2
            temp.append(copy_eggs[:])
            count += 1
            A,B,C = sorted(list(total_set),key= lambda x : copy_eggs[x])
    A,B,C = sorted(list(total_set),key= lambda x : copy_eggs[x])
    while copy_eggs[C] and copy_eggs[B]:
        copy_eggs[C] -= 1
        copy_eggs[B] -= 1
        copy_eggs[D] += 2
        temp.append(copy_eggs[:])
        count += 1
        A,B,C = sorted(list(total_set),key= lambda x : copy_eggs[x])
    if count<min_value:
        min_value = count
        result = [eggs[:]]

        for row in temp:
            result.append(row[:])
            if len(result) == K:
                return

while True:
    K = 100000
    import random
    eggs = [random.randint(4,3000) for _ in range(4)]
    while sum(eggs)%2:
        eggs = [random.randint(4,3000) for _ in range(4)]
    flag = False
    result = []
    min_value = float('inf')

    for i in range(4):
        pick_eggs(i)

    for row in result:
        for n in row:
            if n <0:
                flag = True
                print('----')
                break
        if flag:
            break
    if flag:
        print(eggs,sum(eggs))
        for row in result:
            print(*row)
        break