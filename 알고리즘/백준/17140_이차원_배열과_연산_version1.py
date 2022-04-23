import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()
def check():
    if len(arr)>R and len(arr[0])>C:
        if arr[R][C] == K:
            return True
    return False
def calc(arr):
    rotate = False
    if len(arr) < len(arr[0]):
        arr = list(list(map(list,zip(*arr))))
        rotate = True
    new_arr = []
    max_len = 0
    for row in arr:
        row_counter = Counter(row).most_common()
        row_counter.sort(key= lambda x : (x[1],x[0]))
        temp = []
        for val in row_counter:
            if val[0] == 0:
                continue
            temp.extend(val)
        if len(temp) > 100:
            temp = temp[:100]
        if len(temp) > max_len:
            max_len = len(temp)
        new_arr.append(temp)
    for row in range(len(new_arr)):
        if len(new_arr[row]) < max_len:
            new_arr[row].extend([0]*(max_len-len(new_arr[row])))
    if rotate:
        new_arr = list(list(map(list,zip(*new_arr))))


    return new_arr


def solve():
    global arr
    time = 0
    while time<=100:
        if check():
            return time
        arr = calc(arr)
        time += 1
    return -1
R,C,K = map(int,input().split())
R -= 1
C -= 1
arr = [list(map(int,input().split())) for _ in range(3)]

print(solve())
        