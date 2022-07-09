import math
N = int(input())

arr = input()
c = 0
o =1
for i in arr:
	if i == 'C':
		c+=1
	else:
		o += 1

print(math.ceil(c/o))