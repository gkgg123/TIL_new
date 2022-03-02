import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()
def combi2(pick):
    if pick<2:
        return 0
    return pick*(pick-1)/2
def combi3(pick):
    if pick<3:
        return 0
    return (pick)*(pick-1)*(pick-2)/6
N = int(input())
arr = Counter(list(map(int,input().split())))

key_list = list(arr.keys())
key_list.sort()
key_len = len(key_list)
result = 0
prev_result = 0
for ind1 in range(key_len):
    key1 = key_list[ind1]
    for ind2 in range(ind1,key_len):
        key2 = key_list[ind2]
        key3 = -(key1+key2)
        if key3 < key2:
            continue
        if key1 == key2:
            if key1 == key3:
                result += combi3(arr[key1])
            else:
                result += combi2(arr[key1]) * arr[key3]
        else:
            if key1 == key3:
                result += (arr[key2]*combi2(arr[key1]))
            elif key2 == key3:
                result += (arr[key1]*combi2(arr[key2]))
            else:
                result += arr[key1]*arr[key2]*arr[key3]
print(int(result))