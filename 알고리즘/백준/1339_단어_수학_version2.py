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
list_of_alpha =  list(total.values())
num = 9
list_of_alpha.sort(reverse=True)

for k in list_of_alpha:
    result = result + k*num
    num -= 1
print(result)