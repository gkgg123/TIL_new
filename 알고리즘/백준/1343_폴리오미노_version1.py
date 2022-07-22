arr = input()


while arr.count('XXXX'):
	arr = arr.replace('XXXX','AAAA')
	
while arr.count('XX'):
	arr = arr.replace('XX','BB')
	
if arr.count('X'):
	print(-1)
else:
	print(arr)