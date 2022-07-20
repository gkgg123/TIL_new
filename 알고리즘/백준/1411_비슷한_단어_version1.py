import sys

input = sys.stdin.readline
def al(s):
	return ord(s)-ord('a')
def check(a,b):
	if len(a) != len(b):
		return False
	
	
	max_len = len(a)
	
	for i in range(max_len):
		w1 = al(a[i])+1
		w2 = al(b[i])+1
		if not vi1[w1] and not vi2[w2]:
			vi1[w1] = w2
			vi2[w2] = w1
		elif vi1[w1] != w2 or vi2[w2] != w1:
			return False
	return True
			
	
		
n = int(input())

words = [list(input().strip()) for _ in range(n)]
answer = 0
for ind1 in range(n-1):
	for ind2 in range(ind1+1,n):
		vi1 = [0 for i in range(27)]
		vi2 = [0 for i in range(27)]
		kk =check(words[ind1],words[ind2])
		if kk:
			answer +=1
print(answer)