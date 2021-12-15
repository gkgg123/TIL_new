import sys
from collections import Counter
def input():
    return sys.stdin.readline().rstrip()

cnt = 0
total_dict = Counter()
while True:
    name = input()
    if not name:
        break
    total_dict[name] += 1
    cnt += 1

key_list = sorted(total_dict.keys())

for key in key_list:
    print(f'{key} {total_dict[key]*100/cnt:.4f}')