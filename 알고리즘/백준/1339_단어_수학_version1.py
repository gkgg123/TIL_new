from itertools import permutations
from collections import defaultdict

N = int(input())
alphabet = set()
total = defaultdict(int)
for _ in range(N):
    temp = list(input())
    alphabet.update(temp)
    temp.reverse()
    num = 1
    for k in temp:
        total[k] += num
        num*= 10

result = 0
alphabet = list(alphabet)

num_list = list(range(10-len(alphabet),10))
for new_nums in permutations(num_list):
    temp = 0
    ind = 0
    for key in total.keys():
        temp += total[key]*new_nums[ind]
        ind += 1
    result = max(result,temp)
        

print(result)