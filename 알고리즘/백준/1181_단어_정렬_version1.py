n = int(input())

arr = list(set([input() for _ in range(n)]))
arr.sort(key= lambda x : (len(x),x))
print('\n'.join(arr))