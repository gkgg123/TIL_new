from itertools import combinations

L,C = map(int,input().split())

input_value = list(input().split())

input_value.sort()
vowel = set(['a','e','i','o','u'])
for combi in combinations(input_value,L):
    password = set(combi)
    if password & vowel:
        if len(password-vowel)>=2:
            print(''.join(combi)) 