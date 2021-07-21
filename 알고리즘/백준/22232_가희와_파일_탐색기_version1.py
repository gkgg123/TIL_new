import sys

def input():
    return sys.stdin.readline().rstrip()


N,M = map(int,input().split())

input_list = [list(input().split('.')) for _ in range(N)]

extention_list = set([input() for _ in range(M)])

sort_list = []

for filename,extention in input_list:
    temp = filename + ('.|' if extention in extention_list else '.') + extention
    sort_list.append(temp)

sort_list.sort()

for filename in sort_list:
    filename = filename.replace('|','')
    sys.stdout.write(f'{filename}\n')
